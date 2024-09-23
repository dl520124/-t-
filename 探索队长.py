import numpy as np
import pyautogui
import win32api
import win32con
import win32gui
import win32ui
from liuxingIT2 import LiuXingIT2
import liuxingIT
import time
import random

# 这里可以使用 liuxingIT 模块中的函数和类


if __name__ == '__main__':

    def bezier(p0, p1, p2, t):
        u = 1 - t
        return u ** 2 * p0 + 2 * u * t * p1 + t ** 2 * p2

    xiaoguai = './tansuo/xiaoguai.png'
    boss = './tansuo/boss.png'
    jiesuan1 = './tansuo/jiesuan1.png'
    jiesuan2 = './tansuo/jiesuan2.png'
    neibaoxiang = './tansuo/neibaoxiang.png'
    queren = './tansuo/queren.png'
    k28 = './tansuo/k28.png'
    k2 = './tansuo/k2.png'
    k4 = './tansuo/k4.png'
    k5 = './tansuo/k5.png'
    k7 = './tansuo/k7.png'
    k9 = './tansuo/k9.png'
    k10 = './tansuo/k10.png'
    k17 = './tansuo/k17.png'
    tansuo = './tansuo/tansuo.png'
    duiyou = './tansuo/duiyou.png'
    wutili = './tansuo/wutili.png'

    yingbing = './tansuo/yingbing.png'

    # 悬赏
    xuanshang = './huodong/xuanshang.png'
    gouxie = './huodong/gouxie.png'
    jieshou = './huodong/jieshou.png'
    jujue = './huodong/jujue.png'

    yao = './tansuo/yao.png'
    weizhi1 = './tansuo/weizhi1.png'
    waibaoxiang = './tansuo/waibaoxiang.png'
    waibaoxiang2 = './tansuo/waibaoxiang2.png'
    tuichu = './tansuo/tuichu.png'
    tili = './tansuo/tili.png'
    ji57 = './jiesuan/57ji.png'

    queding = './jiesuan/queding.png'
    tiaozhan = './yuhun/tiaozhan.png'


    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT2(h)
    number = 0;
    baonum =0;
    sainum = 0;
    bossStop = 0;
    while True:

        x, y, p = tt.locateImg(ji57)
        if p > 0.95:
            print("已经57级")
            break

        # time.sleep(1)
        # 悬赏
        x, y, p = tt.locateImg(xuanshang)
        if p > 0.85:
            x, y, p = tt.locateImg(gouxie)
            if p > 0.85:
                x, y, p = tt.locateImg(jieshou)
                if p > 0.85:
                    tt.mouseClick(x, y, 'left')
                    print('接了勾协')
            else:
                x, y, p = tt.locateImg(jujue)
                if p > 0.85:
                    tt.mouseClick(x, y, 'left')
                    print('哪个傻逼给我其他悬赏')
        x, y, p = tt.locateImg(yingbing, None)
        if p > 0.85:
            print('探索里面')
            time.sleep(1)
            x, y, p = tt.locateImg(boss, None)
            if p < 0.80:
                x, y, p = tt.locateImg(xiaoguai, None)
                if p > 0.80:
                    x = random.randint(x - 15, x + 15)
                    y = random.randint(y - 15, y + 15)
                    tt.mouseClick(x, y, 'left')
                    print('找到小怪,点击了:', x, y)
                    sainum = 0;
                else:
                    # time.sleep(2)
                    x, y, p = tt.locateImg(neibaoxiang, None)
                    if p > 0.80:
                        print('有内宝箱')
                        # time.sleep(1)
                        x, y, p = tt.locateImg(queren, None)
                        if p < 0.85:
                            x = random.randint(40, 75)
                            y = random.randint(40, 75)
                            tt.mouseClick(x, y)
                            print('点击返回')
                        # time.sleep(1.5)
                        x, y, p = tt.locateImg(queren, None)
                        if p > 0.85:
                            x = random.randint(718, 835)
                            y = random.randint(390, 420)
                            tt.mouseClick(x, y)
                            print('点击确认')
                    else:
                        # time.sleep(1.5)
                        x, y, p = tt.locateImg(queren, None)
                        if p > 0.85:
                            x = random.randint(718, 835)
                            y = random.randint(390, 420)
                            tt.mouseClick(x, y)
                            print('点击确认')
                        x, y, p = tt.locateImg(yingbing, None)
                        if p > 0.85:
                            print('没有内宝箱也找不到小怪且在探索画面')
                            x, y, p = tt.locateImg(weizhi1, None)
                            print('bossStop',bossStop)
                            if p < 0.85 and bossStop == 0:
                                # 起始点、控制点和结束点
                                x1 = random.randint(1000, 1200)
                                y1 = random.randint(150, 180)

                                x2 = random.randint(600, 800)
                                y2 = random.randint(200, 400)

                                x3 = random.randint(200, 400)
                                y3 = random.randint(100, 300)
                                print('起始坐标', x1, y1)
                                print('控制坐标', x2, y2)
                                print('结束坐标', x3, y3)

                                start_point = np.array([x1, y1])
                                control_point = np.array([x2, y2])
                                end_point = np.array([x3, y3])

                                # 生成一系列参数值
                                num = random.randint(10, 50)
                                t_values = np.linspace(0, 1, num=num)
                                print('贝塞尔num', num)

                                # 计算贝塞尔曲线上的点
                                points = [bezier(start_point, control_point, end_point, t) for t in t_values]

                                # 定义鼠标按下和释放的消息常量
                                WM_LBUTTONDOWN = 0x0201
                                WM_LBUTTONUP = 0x0202
                                # 遍历贝塞尔曲线上的点
                                for point in points:
                                    x, y = int(point[0]), int(point[1])
                                    # 发送鼠标移动消息
                                    win32api.PostMessage(h, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x, y))
                                    # 发送鼠标左键按下消息
                                    win32api.PostMessage(h, WM_LBUTTONDOWN, win32con.MK_LBUTTON,
                                                         win32api.MAKELONG(x, y))
                                    time.sleep(random.uniform(0.01, 0.03))  # 控制每个点之间的时间间隔
                                # 发送鼠标左键释放消息
                                win32api.PostMessage(h, WM_LBUTTONUP, 0, 0)
                                # time.sleep(1)
                                sainum = sainum + 1;

                                if sainum >= 3:
                                    print('滑动超过3次，退出')
                                    x = random.randint(40, 75)
                                    y = random.randint(40, 75)
                                    tt.mouseClick(x, y)
                                    print('点击返回')
                                    # time.sleep(1.5)
                                    x, y, p = tt.locateImg(queren, None)
                                    if p > 0.85:
                                        x = random.randint(718, 835)
                                        y = random.randint(390, 420)
                                        tt.mouseClick(x, y)
                                        print('点击确认')

                            else:
                                print('识别未知1')
                                x = random.randint(40, 75)
                                y = random.randint(40, 75)
                                tt.mouseClick(x, y)
                                print('点击返回')
            else:
                x = random.randint(x - 15, x + 15)
                y = random.randint(y - 5, y + 5)
                tt.mouseClick(x, y, 'left')
                print('找到boss,点击了:', x, y)
                bossStop = 1;

            x, y, p = tt.locateImg(tili)
            if p > 0.85:
                print('体力不足')
                break


        else:
            print('找不到樱饼')

        x, y, p = tt.locateImg(tiaozhan)
        x1, y1, p1 = tt.locateImg(duiyou)
        if p > 0.95 and p1 <0.85:
            # 设置均值和标准差
            mu_x, sigma_x = 1186, 15  # x坐标的均值和标准差
            mu_y, sigma_y = 630, 10  # y坐标的均值和标准差
            # mu_x, sigma_x = 1031.5, 15  # x坐标的均值和标准差
            # mu_y, sigma_y = 574, 10  # y坐标的均值和标准差

            # 生成符合正态分布的坐标点
            x = np.random.normal(mu_x, sigma_x)
            y = np.random.normal(mu_y, sigma_y)

            # 限制坐标范围
            x = np.clip(x, 1150, 1222)
            y = np.clip(y, 596, 664)
            # x = np.clip(x, 1000, 1063)
            # y = np.clip(y, 547, 601)
            tt.mouseClick(x, y, 'left')
            print('点击挑战x=', x, 'y=', y)



        x, y, p = tt.locateImg(jiesuan1)
        if p > 0.80:
            # 生成符合指定范围的正态分布的 x 和 y 坐标
            mu, sigma = 1200, 30  # 均值和标准差
            x = np.random.normal(mu, sigma)
            while x < 1144 or x > 1256:
                x = np.random.normal(mu, sigma)

            mu, sigma = 437, 100  # 均值和标准差
            y = np.random.normal(mu, sigma)
            while y < 185 or y > 689:
                y = np.random.normal(mu, sigma)
            tt.mouseClick(x, y, 'left')
            print('结算1点击x=', x, 'y=', y)
            # time.sleep(1)
            number = number + 1;
            print('number=', number);

        x, y, p = tt.locateImg(jiesuan2)
        if p > 0.85:
            # time.sleep(1)
            # 生成符合指定范围的正态分布的 x 和 y 坐标
            mu, sigma = 1200, 30  # 均值和标准差
            x = np.random.normal(mu, sigma)
            while x < 1144 or x > 1256:
                x = np.random.normal(mu, sigma)

            mu, sigma = 437, 100  # 均值和标准差
            y = np.random.normal(mu, sigma)
            while y < 185 or y > 689:
                y = np.random.normal(mu, sigma)
            tt.mouseClick(x, y, 'left')
            print('结算2点击x=', x, 'y=', y)
            time.sleep(1.5)

        x, y, p2 = tt.locateImg(queding)
        if p2 > 0.85:
            x = random.randint(x - 15, x + 15)
            y = random.randint(y - 5, y + 5)
            tt.mouseClick(x, y)
            bossStop = 0
            print('点击确定')

        x, y, p2 = tt.locateImg(wutili)
        if p2 > 0.85:
            break

        if number>=116:
            break


