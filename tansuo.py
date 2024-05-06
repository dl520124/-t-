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


    # 起始点、控制点和结束点
    start_point = np.array([1089, 155])
    control_point =np.array([766, 240])
    end_point = np.array([296, 188])

    # 生成一系列参数值
    t_values = np.linspace(0, 1, num=100)

    # 计算贝塞尔曲线上的点
    points = [bezier(start_point, control_point, end_point, t) for t in t_values]

    xiaoguai = './tansuo/xiaoguai.png'
    boss = './tansuo/boss.png'
    jiesuan1 = './tansuo/jiesuan1.png'
    jiesuan2 = './tansuo/jiesuan2.png'
    neibaoxiang = './tansuo/neibaoxiang.png'
    queren = './tansuo/queren.png'
    k28 = './tansuo/k28.png'
    tansuo = './tansuo/tansuo.png'
    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12-1')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT(h)
    x = 0
    while True:
        time.sleep(1)
        tt.shot()
        x, y, p = tt.locateImg(boss, None)
        if p<0.85:
            x,y,p = tt.locateImg(xiaoguai,None)
            if p>0.85:
                x = random.randint(x-15,x+15)
                y = random.randint(y-15,y+15)
                tt.mouseClick(x,y,'left')
                print('找到小怪,点击了:',x,y)
                while True:
                    if x > 5:
                        break
                    time.sleep(0.5)
                    x, y, p = tt.locateImg(jiesuan1, None)
                    if p > 0.85:
                        tt.mouseClick(x, y, 'left')
                        print('点击结算1')
                    else:
                        x = x+1
                        pass
                    x, y, p = tt.locateImg(jiesuan2, None)
                    if p > 0.85:
                        time.sleep(1)
                        tt.mouseClick(x, y, 'left')
                        print('点击结算2')
                        break
                    else:
                        x = x + 1
                        pass
            else:
                print('找不到小怪，该滑动了')
                time.sleep(3)
                x, y, p = tt.locateImg(xiaoguai, None)
                x1, y1, p1 = tt.locateImg(boss, None)
                x2, y2, p2 = tt.locateImg(k28, None)
                x3, y3, p3 = tt.locateImg(tansuo, None)
                x4, y4, p4 = tt.locateImg(neibaoxiang, None)
                x5, y5, p5 = tt.locateImg(queren, None)
                if p <0.85 and p1<0.85 and p2 <0.85 and p3<0.85 and p4<0.85 and p5<0.85:
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

                        time.sleep(0.01)  # 控制每个点之间的时间间隔

                    # 发送鼠标左键释放消息
                    win32api.PostMessage(h, WM_LBUTTONUP, 0, 0)
                else:
                   pass
                pass
        else:
            x = random.randint(x - 15, x + 15)
            y = random.randint(y - 15, y + 15)
            tt.mouseClick(x, y, 'left')
            print('找到boss,点击了:', x, y)
            while True:
                time.sleep(0.5)
                x, y, p = tt.locateImg(jiesuan1, None)
                if p > 0.85:
                    tt.mouseClick(x, y, 'left')
                    print('点击结算1')
                else:
                    pass
                x, y, p = tt.locateImg(jiesuan2, None)
                if p > 0.85:
                    time.sleep(1)
                    tt.mouseClick(x, y, 'left')
                    tt.mouseClick(x, y, 'left')
                    print('点击结算2')
                    break
                else:
                    pass
        x, y, p = tt.locateImg(neibaoxiang, None)
        print('判断内宝箱')
        if  p>0.85:
            x = random.randint(40,75)
            y = random.randint(40, 75)
            tt.mouseClick(x,y)
            print('点击返回')
        else:
            pass
        x, y, p = tt.locateImg(queren, None)
        print('判断确认')
        if p > 0.85:
                x = random.randint(718, 835)
                y = random.randint(390, 420)
                tt.mouseClick(x, y)
                print('点击确认')
        else:
            pass
        x, y, p = tt.locateImg(k28, None)
        print('判断K28')
        if  p>0.85:
            x = random.randint(1075,1228)
            y = random.randint(566, 632)
            tt.mouseClick(x,y)
        else:
            pass
        x, y, p = tt.locateImg(tansuo, None)
        print("判断探索")
        if  p>0.85:
            x = random.randint(900,986)
            y = random.randint(523, 553)
            tt.mouseClick(x,y)
        else:
            pass

