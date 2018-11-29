'''
COCO 2017 数据集
示例：
root = 'E:/Data/coco/'
f = ZFile(root)

f.bunch.keys()

stuffZ = f.bunch.stuff_annotations_trainval2017.Z

train_stuffZ = get_content(stuffZ,  'annotations/stuff_train2017_pixelmaps.zip')

print(train_stuffZ)

X = get_content(train_stuffZ, 'stuff_train2017_pixelmaps/000000013992.png')

%pylab inline 
plt.imshow(X)
plt.show()
'''

from collections import defaultdict
import zipfile
import os
import time
import json

import numpy as np
import cv2

from pycocotools.coco import COCO


def buffer2array(Z, filename):
    '''
    将 buffer 转换为 np.uint8 数组
    '''
    buffer = Z.read(filename)
    image = np.frombuffer(buffer, dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


def get_content(Z, filename, is_estract=None):
    '''
    返回 Z 下 filename 的数据
    '''
    if filename.endswith('.json'):
        if is_estract:
            K = Z.extract(filename, 'D:/coco/')
        else:
            print('loading annotations into memory...')
            start = time.clock()
            with Z.open(filename) as fp:
                K = json.load(fp)
            print('Done (t = %gs)' % (time.clock() - start))
        return K
    elif filename.endswith('.jpg') or filename.endswith('.png'):
        return buffer2array(Z, filename)
    elif zipfile.is_zipfile(filename):
        path = Z.extract(filename, 'D:/coco/')
        return zipfile.ZipFile(path)   # 返回 ZipFile 对象


class Bunch(dict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.__dict__ = self


class NameBunch:
    def __init__(self, root):
        '''
        建立一个 root 下的所有由 ZIP 文件组成的 Bunch 对象
        '''
        self.B = Bunch
        self.root = root
        self.name2bunch = self.__nameBunch()

    def __nameBunch(self):
        
        bunch = self.B()
        for name in os.listdir(self.root):
            if zipfile.is_zipfile(self.root + name):
                dataType, _ = os.path.splitext(name)
                bunch[dataType] = self.B({
                    'Z': zipfile.ZipFile(self.root + name)
                    })
        return bunch


class ZFile:
    def __init__(self, Z):
        self.B = Bunch
        Images = [filename for filename, file in Z.NameToInfo.items() \
        if not (file.is_dir() or filename.endswith('.txt'))]
        Anns = [filename for filename in Z.namelist() if filename.endswith('.txt')]
        self.Z2B = self.B(Images=Images, Anns=Anns)


class COCOX(COCO):
    def __init__(self, annZ, annotation_name):
        """
        改写了微软提供的 COCO API 
        使用该 API 可直接读取 ZIP 文件而无须解压
        """
        super().__init__()
        self.B = Bunch
        self.dataset = self.B(get_content(annZ, annotation_name))
        self.createIndex()
    
