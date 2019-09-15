# 数据处理相关 API

[![GitHub issues](https://img.shields.io/github/issues/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/issues) [![GitHub forks](https://img.shields.io/github/forks/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/network) [![GitHub stars](https://img.shields.io/github/stars/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/stargazers) [![GitHub license](https://img.shields.io/github/license/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/blob/master/LICENSE) [![HitCount](http://hits.dwyl.io/DataLoaderX/datasetsome.svg)](http://hits.dwyl.io/DataLoaderX/datasetsome)

在线编辑：[DataLoaderX/datasetsome](https://mybinder.org/v2/gh/DataLoaderX/datasetsome/master)

## 1  CASIA 脱机和在线手写汉字库

API：[xhw.py](dataloader/xhw.py)

关于该数据集的使用可参考如下：

- [使用 python 获取 CASIA 脱机和在线手写汉字库](https://www.imooc.com/article/40759)
- [python 获取 CASIA 脱机和在线手写汉字库 （二）](https://www.imooc.com/article/40914)
- [MPF(Bunch) 转换为 HDF5](https://www.imooc.com/article/41340)
- [python 获取 CASIA 脱机和在线手写汉字库 （三）](https://www.imooc.com/article/288858)

## 2  Omniglot

该数据集的详细介绍，可参考 [omniglot/README.md](./omniglot/README.md)

## 3  COCO

COCO 数据集的使用详见 [COCO 数据集的使用](https://www.cnblogs.com/q735613050/p/8969452.html)和 [COCO 数据集使用说明书](https://www.cnblogs.com/q735613050/p/9888732.html)。 为了更加方便使用 COCO 数据集，我利用 Python 的 `zipfile` 模块写了一个无需解压，直接获取你需要信息的 API：[cocox](https://codexzone.github.io/cocox/)。

## 4 未整理

### 4.1 细粒度识别常用数据集

- [Caltech-UCSD Birds-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)
- [FGVC-Aircraft Benchmark](http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/)
- [Stanford Cars Dataset](https://www.kaggle.com/jessicali9530/stanford-cars-dataset)
