## COCO 数据集

COCO 数据集的使用详见 [COCO 数据集的使用](https://www.cnblogs.com/q735613050/p/8969452.html) 和 [COCO 数据集使用说明书](https://www.cnblogs.com/q735613050/p/9888732.html)。为了更加方便使用 COCO 数据集，我利用 Python 的 `zipfile` 模块写了一个无需解压，直接获取你需要信息的 API：[cocox](https://github.com/Xinering/cocoapi/blob/master/PythonAPI/pycocotools/cocoz.py)。由于直接 fork 微软官方提供的 COCO API，在 Linux 系统下可以无痛使用，但是在 Windows 系统下则会报各种 Bug。为了解决这一难题并以尽可能小的代价去修改代码，我直接借助 Python 的类继承功能，写了一个 COCO API 的子类，该子类很好的支持了 Windows 系统（当然也支持 linux）。

`cocoz.py` 不仅仅提供了对 Windows 的支持，同时该 API 是直接对 COCO 的 `images` 和 `annotations` 中的压缩文件（`.zip`）直接操作，无需直接或间接解压文件（直接跳过解压这一步骤）。

我的 GitHub 上 [Xinering/cocoapi](https://github.com/Xinering/cocoapi) 可以直接下载使用（按照 [Makefile](https://github.com/Xinering/cocoapi/blob/master/PythonAPI/Makefile) 提示进行操作即可）。为了更好的说明如何使用 cocoz 该库提供了两个测试 demo：[pycocoZDemo.ipynb](https://github.com/Xinering/cocoapi/blob/master/PythonAPI/pycocoZDemo.ipynb) 和 [pycocoZEvalDemo.ipynb](https://github.com/Xinering/cocoapi/blob/master/PythonAPI/pycocoZEvalDemo.ipynb)。

关于 RLE 格式的数据，可参考[RLE_decode.ipynb](RLE_decode.ipynb)和[RLE.ipynb](RLE.ipynb)。
