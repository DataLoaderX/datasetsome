## 数据集简介

[Omniglot](https://github.com/brendenlake/omniglot) 数据集包含来自 $50$ 个不同字母的 $1623$ 个不同手写字符。每一个字符都是由 $20$ 个不同的人通过亚马逊的 Mechanical Turk 在线绘制的。

每个图像的轨迹对应于坐标序列为 $[x, y, t]$, 且时间 $(t)$ 以毫秒为单位。笔画数据仅在 MATLAB 文件中可用。

数据集的引用: [Lake, B. M., Salakhutdinov, R., and Tenenbaum, J. B. (2015). Human-level concept learning through probabilistic program induction.](http://www.sciencemag.org/content/350/6266/1332.short) _Science_, 350(6266), 1332-1338.

我们感谢书写系统的 [Omniglot](http://www.omniglot.com/) 百科全书, 它帮助使这一数据集成为可能, 并感谢 [Jason Gross](https://people.csail.mit.edu/jgross/) 对开发和收集这一数据集做出的贡献。

Omniglot 数据集总共包含 $50$ 个字母。我们通常将这些分成一组包含 $30$ 个字母的背景（background）集和一组包含 $20$ 个字母的评估（evaluation）集。

更具挑战性的表示学习任务是使用较小的背景集 "background small 1" 和 "background small 2"。每一个都只包含 $5$ 个字母, 更类似于一个成年人在学习一般的字符时可能遇到的经验。我们的论文在 $30$ 个背景字母报告了的一大组结果, 以及这些更小、更具挑战性的背景集的几个模型的结果。

### MATLAB

- Key data files (images and strokes):
- data_background.mat
- data_evaluation.mat
- data_background_small1.mat
- data_background_small2.mat

要与原文中的 one-shot 分类结果进行比较, 请在 `one-shot-classification` 文件夹中运行 `demo_classification`, 以使用修改后的 Hausdorff 距离演示（demo）基准（baseline）模型。

### PYTHON

- Key data files (images only):
- images_background.zip
- images_evaluation.zip
- images_background_small1.zip
- images_background_small2.zip

要与原论文中的 one-shot 分类结果进行比较, 请查看 [`test_demo.ipynb`](./test_demo.ipynb) 以使用修改的 Hausdorff 距离演示基准模型。

该 API 的详细介绍见：[one-shot 的标准数据集——Omniglot](https://www.imooc.com/article/258879).

更多参考文献解读见 [Reading](./Reading/README.md).