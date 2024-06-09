import os,time,shutil
import pyautogui
import win32gui
import time
import cv2
from liuxingIT import LiuXingIT
import random
import numpy as np



if __name__ == '__main__':

  targetdir = r"F:\yys\阴阳师百鬼夜行\data"

  # 悬赏
  xuanshang = './huodong/xuanshang.png'
  gouxie = './huodong/gouxie.png'
  jieshou = './huodong/jieshou.png'
  jujue = './huodong/jujue.png'


files = []
handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
print(handle)
h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
print(h)
tt = LiuXingIT(h)


def mouse_click(x, y):
    tt.mouseClick(x, y, 'left')
    print(f'点击坐标 x={x}, y={y}')

while True:

    # 悬赏
    x, y, p = tt.locateImg(xuanshang)
    if p > 0.85:
        x, y, p = tt.locateImg(gouxie)
        if p > 0.85:
            x, y, p = tt.locateImg(jieshou)
            if p > 0.85:
                mouse_click(x, y)
            else:
                x, y, p = tt.locateImg(jujue)
                if p > 0.85:
                    mouse_click(x, y)
                    print('哪个傻逼给我其他悬赏')

    files = os.listdir(targetdir)
    for fileitem in files:
        fileroute = os.path.join(targetdir, fileitem)
        if os.path.isfile(fileroute):
            os.remove(fileroute)
        elif os.path.isdir(fileroute):
            shutil.rmtree(fileroute,True)
    print("%s 目录文件和文件夹删除成功" % (time.strftime("%Y/%m/%d %H:%M:%S")))
    time.sleep(60)
