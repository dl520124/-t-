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
    san = './baigui/san.png'
    tubi = './baigui/tubi.png'
    xuanguiwang = './baigui/xuanguiwang.png'


    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT(h)
    while True:
        x, y, p = tt.locateImg(jinru, None)
        if p > 0.85:
            x = random.randint(1078, 1135)
            y = random.randint(580, 627)
            print('jinru')
            tt.mouseClick(x, y, 'left')
        else:
            pass
        x, y, p = tt.locateImg(xuanguiwang, None)
        if p > 0.85:
            x = random.randint(991, 1043)
            y = random.randint(449, 533)
            tt.mouseClick(x, y, 'left')
            x = random.randint(1127, 1206)
            y = random.randint(580, 629)
            print('xuanguiwang')
            tt.mouseClick(x, y, 'left')



        else:
            pass
        x, y, p = tt.locateImg(jiesu, None)
        if p > 0.85:
            x = random.randint(211, 1127)
            y = random.randint(653, 707)
            tt.mouseClick(x, y, 'left')
            print('jiesu')
            time.sleep(4)
        else:
            pass

        x, y, p = tt.locateImg(guilei, None)
        if p > 0.7:
            print('guilei')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(jiuciliang, None)
        if p > 0.7:
            print('jiuciliang')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(ndeng, None)
        if p > 0.7:
            print('ndeng')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(ndenglong, None)
        if p > 0.7:
            print('ndenglong')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(ngu, None)
        if p > 0.7:
            print('ngu')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nhong, None)
        if p > 0.7:
            print('nhong')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nhonggui, None)
        if p > 0.7:
            print('nhonggui')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nlv, None)
        if p > 0.7:
            print('nlv')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(nsaoba, None)
        if p > 0.7:
            print('nsaoba')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(san, None)
        if p > 0.7:
            print('san')
            tt.mouseClick(x, y, 'left')

        else:
            pass
        x, y, p = tt.locateImg(tubi, None)
        if p > 0.7:
            print('tubi')
            tt.mouseClick(x, y, 'left')

        else:
            pass
