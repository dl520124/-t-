import matplotlib.pyplot as plt
import numpy as np
# 定义一个生成随机坐标的函数
def generate_coordinates(mu_x=1200, sigma_x=30, mu_y=437, sigma_y=100):
    # 生成符合正态分布的x坐标
    x = np.random.normal(mu_x, sigma_x)
    # 如果x坐标不在指定范围内，就继续生成
    while x < 1144 or x > 1256:
        x = np.random.normal(mu_x, sigma_x)
    # 生成符合正态分布的y坐标
    y = np.random.normal(mu_y, sigma_y)
    # 如果y坐标不在指定范围内，就继续生成
    while y < 185 or y > 689:
        y = np.random.normal(mu_y, sigma_y)
    # 返回生成的x和y坐标
    return x, y
# 运行并绘制图像
def run_and_plot(n=1000):
    x_coordinates = []  # x坐标列表
    y_coordinates = []  # y坐标列表
    for _ in range(n):
        x, y = generate_coordinates()  # 生成坐标
        x_coordinates.append(x)  # 将x坐标添加至列表
        y_coordinates.append(y)  # 将y坐标添加至列表
    plt.scatter(x_coordinates, y_coordinates, marker='o')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scatter plot of generated coordinates")
    plt.grid(True)
    plt.show()
run_and_plot()