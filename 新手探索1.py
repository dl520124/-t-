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
    ji53 = './jiesuan/53ji.png'
    buzu3 = './jiesuan/buzu3.png'

    #卡主
    kazhu = './tansuo/kazhu.png'
    tingyuan = './tansuo/tingyuan.png'
    queding = './jiesuan/queding.png'



    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT(h)
    number = 0;
    baonum =0;
    sainum = 0;
    bossnum = 0
    bossStop = 0;

    #探索状态
    tansuo_state = 0

    #时间
    xunhuan_time = 0
    jiesuan_time = 0
    dianxiannum = 0



    while True:
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

        x, y, p = tt.locateImg(boss, None)
        if p > 0.80:
            x = random.randint(x - 15, x + 15)
            y = random.randint(y - 15, y + 15)
            tt.mouseClick(x, y, 'left')
            print('找到boss,点击了:', x, y)

        x, y, p = tt.locateImg(xiaoguai, None)
        if p > 0.80:
            x = random.randint(x - 15, x + 15)
            y = random.randint(y - 15, y + 15)
            tt.mouseClick(x, y, 'left')
            print('找到小怪,点击了:', x, y)

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

        x, y, p = tt.locateImg(tansuo, region=(863, 500, 1020, 576))
        print("判断探索")
        if p > 0.85:
            x = random.randint(900, 986)
            y = random.randint(523, 553)
            tt.mouseClick(x, y)
        else:
            pass



        x, y, p = tt.locateImg(queren, None)
        if p > 0.85:
            x = random.randint(718, 835)
            y = random.randint(390, 420)
            tt.mouseClick(x, y)
            print('点击确认')
            time.sleep(0.5)

        x, y, p = tt.locateImg(tili)
        if p > 0.85:
            print('体力不足')
            break






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
            jiesuan_time = time.time()
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

        x, y, p = tt.locateImg(k28, region=(1000,120,1270,700))
        print('判断K2')
        if p > 0.80:
            x = random.randint(x - 53, x + 88)
            y = random.randint(y, y + 79)
            tt.mouseClick(x, y)
        else:
            pass









