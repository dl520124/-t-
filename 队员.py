import pyautogui
import win32gui
import time
import cv2
from liuxingIT2 import LiuXingIT2
import random
import numpy as np

if __name__ == '__main__':
  jiesuan1 = './huodong/jiesuan1.png'
  jiesuan2 = './huodong/jiesuan2.png'
  jiesuan3 = './jiesuan/jiesuan3.png'
  tiaozhan = './huodong/tiaozhan.png'
  jiangli = './huodong/jiangli.png'

  #悬赏
  xuanshang = './huodong/xuanshang.png'
  gouxie = './huodong/gouxie.png'
  jieshou = './huodong/jieshou.png'
  jujue = './huodong/jujue.png'


  img = cv2.imread('888.bmp')

  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT2(h)


  num = 0;
  xunerr = 0;

  while True:
      xunerr = xunerr+1;

      #悬赏
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
      if p > 0.85:

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
        print('结算1点击x=',x,'y=',y)
        time.sleep(1)
        num = num + 1;
        xunerr = 0;
        print('num=', num);

      x, y, p = tt.locateImg(jiesuan2)
      if p > 0.85:

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
        time.sleep(1)

      # x, y, p = tt.locateImg(jiesuan3)
      # if p > 0.85:
      #
      #   # 生成符合指定范围的正态分布的 x 和 y 坐标
      #   mu, sigma = 1200, 30  # 均值和标准差
      #   x = np.random.normal(mu, sigma)
      #   while x < 1144 or x > 1256:
      #     x = np.random.normal(mu, sigma)
      #
      #   mu, sigma = 437, 100  # 均值和标准差
      #   y = np.random.normal(mu, sigma)
      #   while y < 185 or y > 689:
      #     y = np.random.normal(mu, sigma)
      #   tt.mouseClick(x, y, 'left')
      #   print('结算3点击x=', x, 'y=', y)
      #   time.sleep(1)


      x, y, p = tt.locateImg(jiangli)
      if p > 0.85:
          print('识别奖励')
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
          print('奖励点击x=', x, 'y=', y)
          time.sleep(1)


      # if xunerr>=80:
      #    print('掉线，退出')
      #    break;

      if num>=12:
         print('已经打了',num,'局，结束御魂！')
         break;

