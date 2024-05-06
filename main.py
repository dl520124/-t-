import win32gui

from liuxingIT import LiuXingIT
import time
import random


if __name__ == '__main__':
    xiaoguai = 'tansuo/xiaoguai.png'


    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'nemuwin', 'nemudisplay')
    print(h)
    tt = LiuXingIT(524500)
    while True:
        time.sleep(1)
        tt.shot()
        x,y,p = tt.locateImg(xiaoguai,None)
        if p>0.85:
            x = random.randint(x-15,x+15)
            y = random.randint(y-15,y+15)
            tt.mouseClick(x,y,'left')
            print('找到图片,点击了:',x,y)
        else:
            pass
