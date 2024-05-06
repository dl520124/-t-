
import win32gui
import time
import cv2
from liuxingIT import LiuXingIT
import random

if __name__ == '__main__':
    zhan = './douji/zhan.png'
    zidong = './douji/zidong.png'
    shoudong = './douji/shoudong.png'
    jiesuan = './douji/jiesuan.png'
    zidong2 = './douji/zidong2.png'
    lvbiao = './douji/lvbiao.png'
    sanwei = './douji/sanwei.png'

    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT(h)
    while True:
        x, y, p = tt.locateImg(zhan, None)
        if  p>0.85:
            x = random.randint(x-2,x+3)
            y = random.randint(y-2, y+1)
            tt.mouseClick(x,y)
            print('开始斗鸡')
            time.sleep(1)
        else:
            pass

        x, y, p = tt.locateImg(zidong, None)
        if p > 0.85:
            x = random.randint(x - 2, x + 3)
            y = random.randint(y - 2, y + 1)
            tt.mouseClick(x, y)
            print('上自动阵容')
            time.sleep(1)
        else:
            pass

        x, y, p = tt.locateImg(shoudong, None)
        if p > 0.85:
            x = random.randint(x - 2, x + 3)
            y = random.randint(y - 2, y + 1)
            tt.mouseClick(x, y)
            print('自动')
            time.sleep(1)
        else:
            pass


        x, y, p = tt.locateImg(jiesuan, None)
        if p > 0.85:
            x = random.randint(1122, 1249)
            y = random.randint(583, 679)
            tt.mouseClick(x, y)
            print('结算')
            time.sleep(1)
        else:
            pass

        x, y, p = tt.locateImg(zidong2, None)
        if p > 0.85:
            print('现在是自动斗鸡中')
            x, y, p = tt.locateImg(lvbiao, None)
            if p < 0.85:
                print('没有绿标')
                x, y, p = tt.locateImg(sanwei, None)
                if p > 0.70:
                    tt.mouseClick(x, y)
                    print('点击三尾狐')
                    time.sleep(1)
                else:
                    pass
            else:
                pass
        else:
            pass




