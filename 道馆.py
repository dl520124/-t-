import pyautogui
import win32gui
import time
import cv2
from liuxingIT import LiuXingIT
import random
import numpy as np

if __name__ == '__main__':
  zhunbei = './daoguan/zhunbei.png'
  lvbiao = './daoguan/lvbiao.png'
  hua1 = './daoguan/hua1.png'
  hua2 = './daoguan/hua2.png'
  hua3 = './daoguan/hua3.png'
  hua4 = './daoguan/hua4.png'
  tianzhao = './daoguan/tianzhao.png'
  daoguan = './jiesuan/daoguan.png'
  img = cv2.imread('888.bmp')

  # 悬赏
  xuanshang = './huodong/xuanshang.png'
  gouxie = './huodong/gouxie.png'
  jieshou = './huodong/jieshou.png'
  jujue = './huodong/jujue.png'

  jiesuan1 = './huodong/jiesuan1.png'
  jiesuan2 = './huodong/jiesuan2.png'
  shibai = './huodong/shibai.png'

  handle = win32gui.FindWindow('LDPlayerMainFrame', '雷电模拟器')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'RenderWindow', 'TheRender')
  print(h)
  tt = LiuXingIT(h)

  def mouse_click(x, y):
    tt.mouseClick(x, y, 'left')
    print(f'点击坐标 x={x}, y={y}')
    time.sleep(1)

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

      time.sleep(0.5)
      x, y, p = tt.locateImg(zhunbei)
      print(p)
      if p > 0.89:
          x = random.randint(x, x + 30)
          y = random.randint(y - 15, y + 15)
          mouse_click(x, y)
          print('点击准备')
          time.sleep(1.5)
          x, y, p = tt.locateImg(lvbiao)
          x1, y1, p1 = tt.locateImg(zhunbei)
          print(p)
          if p < 0.80 and p1 < 0.8:
              print('没有找到绿标')
              x, y, p = tt.locateImg(tianzhao)
              x1, y1, p1 = tt.locateImg(zhunbei)
              if p > 0.70 and p1 < 0.8:
                 mouse_click(x, y)
                 print('点击天照')

          else:
              print('有绿标')





      time.sleep(0.5)
      x, y, p = tt.locateImg(daoguan)
      print(p)
      if p > 0.99:
          x = random.randint(x - 30, x + 30)
          y = random.randint(y - 15, y + 15)
          mouse_click(x, y)
          print('点击准备')

      time.sleep(0.5)

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
          print('结算1点击x=', x, 'y=', y)
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






