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
import ctypes

if __name__ == '__main__':
    guilei = './baigui/guilei.png'
    jiesu = './baigui/jiesu.png'
    jinru = './baigui/jinru.png'
    jiuciliang = './baigui/jiuciliang.png'
    kaishi = './baigui/kaishi.png'
    ndeng = './baigui/ndeng.png'
    ndenglong = './baigui/ndenglong.png'
    ngu = './baigui/ngu.png'
    nhong = './baigui/nhong.png'
    nhonggui = './baigui/nhonggui.png'
    nlv = './baigui/nlv.png'
    nsaoba = './baigui/nsaoba.png'
    guinei = './baigui/guinei.png'
    gui0 = './baigui/gui0.png'
    san = './baigui/san.png'
    tubi = './baigui/tubi.png'
    xuanguiwang = './baigui/xuanguiwang.png'


    # handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    # print(handle)
    # h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')

    handle = win32gui.FindWindow('LDPlayerMainFrame', '雷电模拟器')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'RenderWindow', 'TheRender')
    print(h)
    tt = LiuXingIT(h)

    # 自己加的
    # 定义一些需要的常量
    WM_LBUTTONDOWN = 0x0201
    WM_LBUTTONUP = 0x0202
    MK_LBUTTON = 0x0001
    WM_RBUTTONDOWN = 0x0204
    WM_RBUTTONUP = 0x0205
    MK_RBUTTON = 0x0002
    WM_MBUTTONDOWN = 0x0207
    WM_MBUTTONUP = 0x0208
    MK_MBUTTON = 0x0010
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    def MAKELONG(low, high):
        return (high << 16) | (low & 0xFFFF)


    def baiguimouseClick(x, y, button='left', move_left_steps=5, move_distance=20):
        x = int(x)
        y = int(y)
        print(x, y)

        # 按照move_left_steps次点击
        for _ in range(move_left_steps):
            position = MAKELONG(x, y)

            if button == 'left':
                success_down = user32.PostMessageW(h,WM_LBUTTONDOWN, MK_LBUTTON, position)
                if success_down:
                    time.sleep(0.05)  # 延时
                success_up = user32.PostMessageW(h,WM_LBUTTONUP, MK_LBUTTON, position)
                if success_up:
                    time.sleep(0.05)  # 延时
            # 每次点击后，x往左移动 move_distance
            time.sleep(1)
            x -= move_distance




    while True:
        x, y, p = tt.locateImg(jinru, None)
        if p > 0.8:
            x = random.randint(1078, 1135)
            y = random.randint(580, 627)
            print('jinru')
            tt.mouseClick(x, y, 'left')
        else:
            pass
        x, y, p = tt.locateImg(xuanguiwang, None)
        if p > 0.8:
            x = random.randint(991, 1043)
            y = random.randint(449, 533)
            tt.mouseClick(x, y, 'left')
            time.sleep(0.5)
            x = random.randint(1127, 1206)
            y = random.randint(580, 629)
            print('xuanguiwang')
            tt.mouseClick(x, y, 'left')



        else:
            pass
        x, y, p = tt.locateImg(jiesu, None)
        if p > 0.8:
            x = random.randint(211, 1127)
            y = random.randint(653, 707)
            tt.mouseClick(x, y, 'left')
            print('jiesu')
            time.sleep(4)
        else:
            pass

        x, y, p = tt.locateImg(guilei, None)
        if p > 0.8:
            print('guilei')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(jiuciliang, None)
        if p > 0.75:
            print('jiuciliang')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(ndeng, None)
        if p > 0.75:
            print('ndeng')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(ndenglong, None)
        if p > 0.75:
            print('ndenglong')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(ngu, None)
        if p > 0.75:
            print('ngu')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nhong, None)
        if p > 0.75:
            print('nhong')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nhonggui, None)
        if p > 0.75:
            print('nhonggui')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nlv, None)
        if p > 0.75:
            print('nlv')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nsaoba, None)
        if p > 0.75:
            print('nsaoba')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(san, None)
        if p > 0.75:
            print('san')
            baiguimouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(tubi, None)
        if p > 0.75:
            print('tubi')
            baiguimouseClick(x, y, 'left')

        else:
            pass

        x, y, p = tt.locateImg(guinei)
        x1, y1, p1 = tt.locateImg(gui0)
        if p > 0.85 and p1 < 0.85:
            # time.sleep(1)
            # 生成符合指定范围的正态分布的 x 和 y 坐标
            mu, sigma = 1200, 30  # 均值和标准差
            x = np.random.normal(mu, sigma)
            while x < 1000 or x > 1256:
                x = np.random.normal(mu, sigma)

            mu, sigma = 437, 100  # 均值和标准差
            y = np.random.normal(mu, sigma)
            while y < 185 or y > 689:
                y = np.random.normal(mu, sigma)
            tt.mouseClick(x, y, 'left')
            print('结算2点击x=', x, 'y=', y)
