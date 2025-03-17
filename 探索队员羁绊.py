import numpy as np
import pyautogui
import win32api
import win32con
import win32gui
import win32ui
from liuxingIT import LiuXingIT
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
    likai = './tansuo/likai.png'

    yingbing = './tansuo/yingbing.png'

    # 悬赏
    xuanshang = './huodong/xuanshang.png'
    gouxie = './huodong/gouxie.png'
    jieshou = './tansuo/jieshou.png'
    jujue = './huodong/jujue.png'

    yao = './tansuo/yao.png'
    weizhi1 = './tansuo/weizhi1.png'
    waibaoxiang = './tansuo/waibaoxiang.png'
    waibaoxiang2 = './tansuo/waibaoxiang2.png'
    tuichu = './tansuo/tuichu.png'
    tili = './tansuo/tili.png'

    queding = './jiesuan/queding.png'
    buzu3 = './jiesuan/buzu3.png'
    tuichuk28 = './jiesuan/tuichuk28.png'


    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12-2')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT(h)
    number = 0;
    baonum =0;
    sainum = 0;
    bossStop = 0;
    while True:
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
            # time.sleep(1)

        x3, y3, p3 = tt.locateImg(tuichuk28)
        x, y, p2 = tt.locateImg(queding)
        if p2 > 0.85 and p3 > 0.85:
            x = random.randint(x - 15, x + 15)
            y = random.randint(y - 5, y + 5)
            tt.mouseClick(x, y)
            print('点击确定')



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


        # x, y, p = tt.locateImg(buzu3)
        # print(p)
        # if p > 0.94:
        #     print('突破券满了')
        #     break
        # else:
        #     x, y, p = tt.locateImg(jieshou)
        #     if p > 0.95:
        #         tt.mouseClick(x, y, 'left')
        #         print('接受组队')

        x, y, p = tt.locateImg(jieshou)
        if p > 0.95:
            tt.mouseClick(x, y, 'left')
            print('接受组队')

        x, y, p = tt.locateImg(likai, None)
        if p > 0.85:
            x = random.randint(40, 75)
            y = random.randint(40, 75)
            tt.mouseClick(x, y)
            print('点击返回')






        if number>=999:
            break


