from matplotlib import pyplot as plt
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号 '-' 显示为方块的问题


def plot(x):
    x = x.astype(np.uint8)
    plt.imshow(x)
    plt.axis('off')
    plt.show()


def show_imgs(imgs):
    '''
    展示 多张图片
    '''
    imgs = imgs.astype(np.uint8)
    n = imgs.shape[0]
    h, w = 4, int(n / 4)
    _, figs = plt.subplots(h, w, figsize=(32, 32))
    K = np.arange(n).reshape((h, w))
    for i in range(h):
        for j in range(w):
            img = imgs[K[i, j]]
            figs[i][j].imshow(img)
            figs[i][j].axes.get_xaxis().set_visible(False)
            figs[i][j].axes.get_yaxis().set_visible(False)
    plt.show()