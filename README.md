# 数据之家

[![GitHub issues](https://img.shields.io/github/issues/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/issues) [![GitHub forks](https://img.shields.io/github/forks/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/network) [![GitHub stars](https://img.shields.io/github/stars/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/stargazers) [![GitHub license](https://img.shields.io/github/license/DataLoaderX/datasetsome)](https://github.com/DataLoaderX/datasetsome/blob/master/LICENSE) [![HitCount](http://hits.dwyl.io/DataLoaderX/datasetsome.svg)](http://hits.dwyl.io/DataLoaderX/datasetsome) ![GitHub repo size](https://img.shields.io/github/repo-size/DataLoaderX/datasetsome)

本项目主要用于记录与数据处理相关的资源，同时您可以进入 [mybinder: datasetsome](https://mybinder.org/v2/gh/DataLoaderX/datasetsome/master) 进行线编辑。为了将数据和代码以及文档分离，本项目将一些数据集存放在子模块 [SimpleDataset](https://github.com/DatasetLab/SimpleDataset) 之中，而将代码存放在子模块 [loader](https://xinetzone.github.io/loader/) 之中。

## 数据集处理

- [X.h5 数据集的创建和使用](simpledataset/README.md)
- [COCO 数据集](coco/README.md)
- [CASIA 脱机和在线手写汉字库](casia/README.md)
- [omniglot 数据集](omniglot/README.md)
- [待办事项](TODOS/README.md)

## 本项目的使用说明

因为本项目包含子模块，所以在克隆时，您可以选择使用命令：
  
```sh
$ git clone --recursive https://github.com/DataLoaderX/datasetsome
```

直接下载项目并更新仓库中的每一个子模块。

如果您不想在克隆仓库时下载子模块，您只需要运行下面的命令即可：

```
$ git clone https://github.com/DataLoaderX/datasetsome
```

待您将项目下载到您的电脑后，输入命令：

```
$ git submodule init
$ git submodule update
```

拉取子模的更新。
