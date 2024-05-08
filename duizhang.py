import pyautogui
import win32gui
import time
import cv2
from liuxingIT import LiuXingIT
import random
import numpy as np

if __name__ == '__main__':
  jiesuan1 = './huodong/jiesuan1.png'
  jiesuan2 = './huodong/jiesuan2.png'
  jiesuan3 = './jiesuan/jiesuan3.png'
  tiaozhan = './yuhun/tiaozhan.png'
  duiyou2 = './yuhun/duiyou2.png'
  jiangli = './huodong/jiangli.png'


  #悬赏
  xuanshang = './huodong/xuanshang.png'
  gouxie = './huodong/gouxie.png'
  jieshou = './huodong/jieshou.png'
  jujue = './huodong/jujue.png'

  img = cv2.imread('888.bmp')

  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12-1')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT(h)


  num = 0;
  err = 0;

  while True:

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

      #
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

      x, y, p = tt.locateImg(tiaozhan)
      if p > 0.85:
          print('已经找到挑战的图')
          time.sleep(1)
          err = err + 1;
          print('err=',err)
          x, y, p = tt.locateImg(duiyou2,region=(467,136,821,540))#如果找不到则已有队员2进入
          #x, y, p = tt.locateImg(duiyou2, region=(913, 136, 1240, 550))  # 如果找不到则已有队员3进入
          if p > 0.85:
                 print('队员2已经进入')
                 err = 0;
                 # 设置均值和标准差
                 mu_x, sigma_x = 1221.5, 15  # x坐标的均值和标准差
                 mu_y, sigma_y = 643.5, 10  # y坐标的均值和标准差
                 # 如果你希望大部分数据点都落在范围内，可以选择较小的标准差；如果希望数据点更分散，可以选择较大的标准差。

                 # 生成符合正态分布的坐标点
                 x = np.random.normal(mu_x, sigma_x)
                 y = np.random.normal(mu_y, sigma_y)

                 # 限制坐标范围
                 x = np.clip(x, 1193, 1249)
                 y = np.clip(y, 619, 668)
                 tt.mouseClick(x, y, 'left')
                 print('点击挑战x=', x, 'y=', y)
                 time.sleep(2)

      if err>=10:
         print('队友掉线，停止')
         break;


      if num>=200:
         print('已经打了',num,'局，结束御魂！')
         break;


