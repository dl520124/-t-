import numpy as np
import matplotlib.pyplot as plt

# 生成符合正态分布的随机数
mu, sigma = 0, 0.1  # 均值和标准差
s = np.random.normal(mu, sigma, 1000)

# 绘制直方图
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()