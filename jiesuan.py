import pyautogui
import win32gui
import time
import cv2
from liuxingIT import LiuXingIT
import random
import numpy as np

if __name__ == '__main__':
  jiesuan1 = './jiesuan/jiesuan1.png'
  jiesuan2 = './jiesuan/jiesuan2.png'
  tupotu = './jiesuan/tupotu.png'
  jingong = './jiesuan/jingong.png'
  wancheng = './jiesuan/wancheng.png'
  shibai = './jiesuan/shibai.png'
  diancuo = './jiesuan/diancuo.png'

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
  tt = LiuXingIT(h)


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

      x, y, p = tt.locateImg(shibai)
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

      x, y, p = tt.locateImg(diancuo)
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

      x, y, p = tt.locateImg(tupotu)
      if p > 0.85:
        x = random.randint(x-180,  x)
        y = random.randint(y+10, y+80)
        tt.mouseClick(x, y, 'left')
        print('识别突破标志')
        time.sleep(1)

      x, y, p = tt.locateImg(jingong)
      if p > 0.85:
        x = random.randint(x-30,  x+30)
        y = random.randint(y-15, y+15)
        tt.mouseClick(x, y, 'left')
        print('点击进攻')
        time.sleep(1)

      x, y, p = tt.locateImg(wancheng)
      if p > 0.85:
        x, y, p = tt.locateImg(tupotu)
        if  p < 0.85:
              print('突破已完成，不愧是tt，真棒棒！')
              time.sleep(1)
              break

