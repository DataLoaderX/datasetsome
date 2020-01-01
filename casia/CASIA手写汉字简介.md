## CASIA 手写汉字简介

<details>
<summary><b>CASIA-HWDB</b> 和 <b>CASIA-OLHWDB</b> 数据库简称为 CASIA。</summary>
<pre><code>
由中科院自动化研究所在 2007-2010 年间收集；
包含 1 020 人书写的脱机（联机）手写中文单字样本和手写文本；
用 Anoto 笔在点阵纸上书写后扫描、分割得到。
</code></pre>
</details>

CASIA 的使用需要遵循申请书 [CASIA-HWDB](http://www.nlpr.ia.ac.cn/databases/download/CASIA-HWDB-Chinese.pdf) 和 [CASIA-OLHWDB](http://www.nlpr.ia.ac.cn/databases/download/CASIA-OLHWDB-Chinese.pdf)，而数据集的下载请访问 [CASIA Online and Offline Chinese Handwriting Databases](http://www.nlpr.ia.ac.cn/databases/handwriting/Download.html)。

> 本数据库经签约授权后可免费用于学术研究目的，但用于商业目的需付费。学术研究的用途包括手写 文档分割、字符识别、字符串识别、文档检索、书写人适应、书写人鉴别等。

在申请书中介绍了数据集的基本情况：

数据集名称|划分|简介|
:-:|:-:|:-:
CASIA-HWDB |离线手写单字样本分为三个数据库：*HWDB1.0\~1.2*，离线手写文本也分为三个数据库： *HWDB2.0\~2.2*。|HWDB1.0\~1.2 总共有 $3\,895\,135$ 个手写单字样本，分属 $7\,356$ 类（$7\,185$ 个汉字和 $171$ 个英文字母、数字、符号）；HWDB2.0\~2.2 总共有 $5\,091$ 页图像，分割为 $52\,230$ 个文本行和 $1\,349\,414$ 个文字。所有文字和文本样本均存为灰度图像（背景已去除），按书写人序号分别存储。
CASIA-OLHWDB|在线手写单字样本分为三个数据库：*OLHWDB1.0\~1.2*，在线手写文本也分为三个数据库： *OLHWDB2.0\~2.2*。|OLHWDB1.0\~1.2 总共有 $3\,912\,017$ 个手写单字样本，分属 $7,356$ 类（$7\,185$ 个汉字和 $171$ 个英文字母、数字、符号）；OLHWDB2.0\~2.2 总共有 $5\,092$ 页手写文本，分割为 $52\,221$ 个文本行和 $1\,348\,904$ 个文字。所有文字和文本样本均存为笔划坐标序列，按书写人序号分别存储。

CASIA 单字数据库不仅仅提供了单字数据的图片还提供了这些单字数据的特征，并依据 [fileFormat-mpf.pdf](http://www.nlpr.ia.ac.cn/databases/download/feature_data/FileFormat-mpf.pdf) 来保存其特征。简单点说，每个单字的特征均以 `.mpf` 形式保存手工特征。以`_pot` 结尾的压缩文件保存了在线单字的图片信息，而以 `_gnt` 结尾的压缩文件则保存了离线单字的图片信息。


关于该数据集的使用和简介的详细内容可参考博文集 [post.md](post.md)。


