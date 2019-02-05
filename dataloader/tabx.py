'''
整合几个常用的数据集在一个 HDF5 文件中
'''


import pandas as pd
import tables as tb
import numpy as np
import keras


def dataset_to_hdf5(x_train, y_train, x_test, y_test, f):
    '''
    利用 Keras 导出 (x_train, y_train), (x_test, y_test)，例如：
         (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

    f 在下面的列表中：
    ['cifar10', 'cifar100', 'fashion_mnist', 'mnist', 'boston_housing', 'imdb', 'reuters']
    '''
    root = 'E:/Data/HDF5/'
    f1 = 'train_'
    f2 = 'test_'
    filters = tb.Filters(complevel=7, shuffle=False)
    h5 = tb.open_file(root + f + '.h5', 'w', title=f, filters=filters)
    h5.create_group(h5.root, 'train_dataset', title=f1 + f)
    h5.create_group(h5.root, 'test_dataset', title=f2 + f)
    h5.create_array('/train_dataset', 'data', x_train)
    h5.create_array('/train_dataset', 'label', y_train)
    h5.create_array('/test_dataset', 'data', x_test)
    h5.create_array('/test_dataset', 'label', y_test)
    h5.close()


def xin_datasets(root):
    '''
    通过 keras 获取数据集：{'cifar10', 'cifar100', 'fashion_mnist', 'mnist', 'boston_housing'}
    并将其转换为 HDF5 文件
    '''
    names = ['cifar10', 'cifar100', 'fashion_mnist', 'mnist', 'boston_housing']
    f1 = 'train_'
    f2 = 'test_'
    filters = tb.Filters(complevel=7, shuffle=False)
    h5 = tb.open_file(
        root + 'xindatasets' + '.h5',
        'w',
        title='xin datasets',
        filters=filters)
    a1 = keras.datasets.cifar10.load_data()
    a2 = keras.datasets.cifar100.load_data()
    a3 = keras.datasets.fashion_mnist.load_data()
    a4 = keras.datasets.mnist.load_data()
    a5 = keras.datasets.boston_housing.load_data()

    L = [a1, a2, a3, a4, a5]
    for n, name in enumerate(names):
        (x_train, y_train), (x_test, y_test) = L[n]
        h5.create_group('/', name, createparents=True)
        h5.create_group('/' + name, 'train_dataset', title=f1 + name)
        h5.create_group('/' + name, 'test_dataset', title=f2 + name)
        h5.create_array('/' + name + '/train_dataset', 'data', x_train)
        h5.create_array('/' + name + '/train_dataset', 'label', y_train)
        h5.create_array('/' + name + '/test_dataset', 'data', x_test)
        h5.create_array('/' + name + '/test_dataset', 'label', y_test)
    h5.close()


def normalize(X_train, X_valid, is_image=None):
    '''将类 ndarray 数据集做中心化处理，并将数据类型转换为 np.float32'''
    if is_image:
        X_train = np.asanyarray(X_train, dtype=np.float32)
        X_valid = np.asanyarray(X_valid, dtype=np.float32)
        return X_train / 255, X_valid / 255
    else:
        mean = np.mean(X_train, axis=0, dtype=np.float32)
        X_train = X_train - mean
        X_valid = X_valid - mean
        e = 10**(-7)
        var = np.var(X_train, 0, dtype=np.float32) + e
        std = np.sqrt(var)
        return X_train / std, X_valid / std


def get_datasets(name):
    '''
    从数据库中 copy 一份数据到指定位置，防止损坏原始数据
    name in ['cifar10', 'cifar100', 'fashion_mnist', 'mnist', 'boston_housing']
    返回 (X_train, Y_train, X_test, Y_test)，它们可以当作 numpy 和 pandas 使用
    '''
    h5 = tb.open_file('E:/Data/HDF5/xindatasets.h5')
    h5.copy_file('D:/temp/datasets.h5')
    h5.close()
    myh5 = tb.open_file('D:/temp/datasets.h5')
    X_train = myh5.get_node('/' + name + '/train_dataset/data')
    Y_train = myh5.get_node('/' + name + '/train_dataset/label')
    X_test = myh5.get_node('/' + name + '/test_dataset/data')
    Y_test = myh5.get_node('/' + name + '/test_dataset/label')
    return X_train, Y_train, X_test, Y_test


def data_iter(X, Y, batch_size, shuffle=True):
    '''由一个类 array 数据集生成一个迭代器'''
    n = X.shape[0]
    if shuffle:
        # 等价于 rand_index = np.random.choice(n, size= batch_size)
        # 等价于 np.random.shuffle(idx)
        idx = np.random.permutation(n)
    else:
        idx = np.arange(n)
    for i in np.arange(0, n, batch_size):
        j = idx[i:min(i + batch_size, n)]
        yield np.take(X, j, 0), np.take(Y, j, 0)


class DataLoader:
    '''
    name in ['cifar10', 'cifar100', 'fashion_mnist', 'mnist', 'boston_housing']
    将 HDF5 数据库中的数据集转换为迭代器。
    在采用 MXNet 训练结束后，需要运行 `myh5.close()` 关闭数据库。
    '''

    def __init__(self,
                 name,
                 temp_name='datasets',
                 source='E:/Data/HDF5/xindatasets.h5'):
        temp_path = 'D:/temp/' + temp_name + '.h5'
        h5 = tb.open_file(source)
        h5.copy_file(temp_path, overwrite=True)
        h5.close()
        self.myh5 = tb.open_file(temp_path)
        self.X_train = self.myh5.get_node('/' + name + '/train_dataset/data')
        self.Y_train = self.myh5.get_node('/' + name + '/train_dataset/label')
        self.X_test = self.myh5.get_node('/' + name + '/test_dataset/data')
        self.Y_test = self.myh5.get_node('/' + name + '/test_dataset/label')
        self.n_samples = self.X_train.nrows

    def get_iter(self, batch_size):
        '''
        return: train_iter, valid_iter
        '''
        train_iter = data_iter(self.X_train, self.Y_train,
                               batch_size, shuffle=True)
        valid_iter = data_iter(self.X_test, self.Y_test,
                               batch_size, shuffle=False)
        return train_iter, valid_iter

        
class DataLoaderSplit:
    '''
    name in ['cifar10', 'cifar100', 'fashion_mnist', 'mnist', 'boston_housing']
    将 HDF5 数据库中的数据集转换为迭代器。
    训练结束后，需要运行 `myh5.close()` 关闭数据库。

    示例
    =======
    batch_size = 64
    prob = 0.5
    Li = LoaderImage(batch_size, prob)
    train_path, test_path = Li.unzip_lables()
    net = BS()
    resize = 32
    T = TrainerImage(Li, resize)
    '''

    def __init__(self,
                 name,
                 temp_name='datasets',
                 source='E:/Data/HDF5/xindatasets.h5'):
        temp_path = 'D:/temp/' + temp_name + '.h5'
        h5 = tb.open_file(source)
        h5.copy_file(temp_path, overwrite=True)
        h5.close()
        self.myh5 = tb.open_file(temp_path)
        self.X_train = self.myh5.get_node('/' + name + '/train_dataset/data')
        self.Y_train = self.myh5.get_node('/' + name + '/train_dataset/label')
        self.X_test = self.myh5.get_node('/' + name + '/test_dataset/data')
        self.Y_test = self.myh5.get_node('/' + name + '/test_dataset/label')
        self.n_samples = self.X_train.nrows

    def split(self, X_train, Y_train, prob=0.8):
        '''
        首先将训练集划分为训练集和验证集，然后再对数据集做归一化处理。
        prob：训练集(与验证集间)所占的比例，
        返回：train_data, train_label, valid_data, valid_label
        '''
        n = self.n_samples
        num_train = int(prob * n)
        idx = np.random.permutation(n)
        j = idx[:num_train]
        k = idx[num_train:]
        train_data = np.take(X_train, j, 0)
        valid_data = np.take(X_train, k, 0)
        train_label = np.take(Y_train, j, 0)
        valid_label = np.take(Y_train, k, 0)
        return train_data, train_label, valid_data, valid_label

    def get_iter(self, batch_size, prob=0.8):
        '''
        return: train_iter, valid_iter, test_iter
        '''
        train_data, train_label, valid_data, valid_label = self.split(self.X_train, self.Y_train, prob)
        train_iter = data_iter(train_data, train_label, batch_size, shuffle=True)
        valid_iter = data_iter(valid_data, valid_label, batch_size, shuffle=False)
        test_iter = data_iter(self.X_train, self.Y_test, batch_size, shuffle=False)
        return train_iter, valid_iter, test_iter

    
