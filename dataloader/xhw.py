'''
该 API 的使用见：
    1. https://www.imooc.com/article/40759
    2. https://www.imooc.com/article/40914
'''


import os
import sys
import zipfile
import rarfile
import struct, pickle
import pandas as pd
import numpy as np
import tables as tb
import time


def getZ(filename):
    _, end = os.path.splitext(filename)
    if end == '.rar':
        Z = rarfile.RarFile(filename)
    elif end == '.zip':
        Z = zipfile.ZipFile(filename)
    return Z


class Bunch(dict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.__dict__ = self


class MPF(Bunch):
    def __init__(self, fp, *args, **kwds):
        super().__init__(*args, **kwds)
        self.fp = fp
        header_size = struct.unpack('l', self.fp.read(4))[0]
        self.code_format = self.fp.read(8).decode('ascii').rstrip('\x00')
        self.text = self.fp.read(header_size - 62).decode().rstrip('\x00')
        self.code_type = self.fp.read(20).decode('latin-1').rstrip('\x00')
        self.code_length = struct.unpack('h', self.fp.read(2))[0]
        self.data_type = self.fp.read(20).decode('ascii').rstrip('\x00')
        self.nrows = struct.unpack('l', self.fp.read(4))[0]
        self.ndims = struct.unpack('l', self.fp.read(4))[0]

    def __iter__(self):
        m = self.code_length + self.ndims
        for i in range(0, m * self.nrows, m):
            label = self.fp.read(self.code_length).decode('gb18030')
            data = np.frombuffer(self.fp.read(self.ndims), np.uint8)
            yield data, label


class Writer(Bunch):
    def __init__(self, mpf, *args, **kwds):
        '''
        dtype 为 结构数组 array
        可将其转换为 pandas:: pd.DataFrame.from_dict(dict(self.feature))
        '''
        super().__init__(*args, **kwds)
        self.text = mpf.text
        t = np.dtype([('label', 'U', 2), ('feature', np.uint8, 512)])
        self.feature = np.array(
            [(label, feature) for feature, label in iter(mpf)], dtype=t)


class Feature(Bunch):
    def __init__(self, root, set_name, *args, **kwds):
        super().__init__(*args, **kwds)
        filename, end = os.path.splitext(set_name)

        if 'HW' in filename and end == '.zip':
            if '_' not in filename:
                self.name = filename
                Z = getZ(f'{root}{set_name}')
                self._get_dataset(Z)
        else:
            #print(f'{filename}不是我们需要的文件！')
            pass

    def _get_dataset(self, Z):
        for name in Z.namelist():
            if name.endswith('.mpf'):
                writer_ = f"writer{os.path.splitext(name)[0].split('/')[1]}"

                with Z.open(name) as fp:
                    mpf = MPF(fp)
                    wt = Writer(mpf)
                    self[writer_] = wt


class XFeature(Bunch):
    def __init__(self, root, *args, **kwds):
        super().__init__(*args, **kwds)
        for filename in os.listdir(root):
            set_name, end = os.path.splitext(filename)
            if 'HW' in filename and end == '.zip':
                if '_' not in set_name:
                    setname = set_name.replace('.', '')
                    start = time.time()
                    self[setname] = Feature(root, filename)
                    print(f'{time.time() - start}秒，完成字典 {setname} 的创建！')


def bunch2json(bunch, path):
    with open(path, 'wb') as fp:
        pickle.dump(bunch, fp)


def json2bunch(path):
    with open(path, 'rb') as fp:
        X = pickle.load(fp)
    return X