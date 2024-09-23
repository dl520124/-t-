import numpy as np
import pyautogui
import win32gui
import time
import cv2
from liuxingIT2 import LiuXingIT2
import random

if __name__ == '__main__':
  zhunbei = './daoguan/zhunbei.png'
  lvbiao = './daoguan/lvbiao.png'
  tianzhao = './daoguan/tianzhao.png'

  jiesuan1 = './tansuo/jiesuan1.png'
  jiesuan2 = './tansuo/jiesuan2.png'
  shibai = './jiesuan/shibai.png'
  shouci = './jiesuan/shouci.png'
  fenxiang = './jiesuan/fenxiang.png'

  # 悬赏
  xuanshang = './huodong/xuanshang.png'
  gouxie = './huodong/gouxie.png'
  jieshou = './tansuo/jieshou.png'
  jujue = './huodong/jujue.png'

  miwen = './jiesuan/miwen.png'
  yeyuanhuo = './jiesuan/yeyuanhuo.png'

  img = cv2.imread('888.bmp')

  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12-1')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT2(h)

  def mouse_click(x, y):
    tt.mouseClick(x, y, 'left')
    print(f'点击坐标 x={x}, y={y}')
    time.sleep(1)

  num = 0
  while True:

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
          num = num + 1;
          xunerr = 0;
          print('num=', num);


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

      x, y, p = tt.locateImg(shibai)
      if p > 0.85:
         break

      x, y, p = tt.locateImg(fenxiang)
      if p > 0.85:
          break



      x, y, p = tt.locateImg(zhunbei)
      if p > 0.9:
          x = random.randint(x - 30, x + 30)
          y = random.randint(y - 15, y + 15)
          mouse_click(x, y)
          print('点击准备')

      x, y, p = tt.locateImg(miwen)
      if p > 0.50 :
          print('已经找到挑战的图')
          x = random.randint(x-3,x+3)
          y = random.randint(y-3,y+5)
          tt.mouseClick(x, y, 'left')
          print('点击挑战x=', x, 'y=', y)
          time.sleep(2)

      x, y, p = tt.locateImg(yeyuanhuo)
      if p > 0.80:
          print('已经找到挑战的图')
          x = random.randint(x - 3, x + 3)
          y = random.randint(y - 3, y + 5)
          tt.mouseClick(x, y, 'left')
          print('点击挑战x=', x, 'y=', y)
          time.sleep(2)


      if num >=6:
          break







