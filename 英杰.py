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
  jiesuan4 = './huodong/jiesuan4.png'
  shibai = './huodong/shibai.png'
  tiaozhan = './huodong/yingjie.png'
  jiangli = './huodong/jiangli.png'

  #悬赏
  xuanshang = './huodong/xuanshang.png'
  gouxie = './huodong/gouxie.png'
  jieshou = './huodong/jieshou.png'
  jujue = './huodong/jujue.png'

  buzu = './huodong/buzu.png'
  queren = './huodong/queren.png'
  h999 = './huodong/h999.png'

  img = cv2.imread('888.bmp')

  handle = win32gui.FindWindow('LDPlayerMainFrame', '雷电模拟器')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'RenderWindow', 'TheRender')
  print(h)
  tt = LiuXingIT(h)


  #handle =  win32gui.FindWindow(None,'MuMu模拟器12')  #第一个参数是类目（可以不写），第二个参数名字

  num = 0;
  xunerr = 0;

  while True:

      x, y, p = tt.locateImg(queren)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('掉线确认')

      x, y, p = tt.locateImg(h999)
      if p > 0.98:
          print(p)
          print('完成999')
          break

      xunerr = xunerr + 1;
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

      x, y, p = tt.locateImg(jiesuan4)
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
        xunerr = 0;

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
          # 设置均值和标准差
          mu_x, sigma_x = 1186, 15  # x坐标的均值和标准差
          mu_y, sigma_y = 630, 10  # y坐标的均值和标准差
          # mu_x, sigma_x = 1031.5, 15  # x坐标的均值和标准差
          # mu_y, sigma_y = 574, 10  # y坐标的均值和标准差

          # 生成符合正态分布的坐标点
          x = np.random.normal(mu_x, sigma_x)
          y = np.random.normal(mu_y, sigma_y)

          # 限制坐标范围
          x = np.clip(x, 1150, 1222)
          y = np.clip(y, 596, 664)
          # x = np.clip(x, 1000, 1063)
          # y = np.clip(y, 547, 601)
          tt.mouseClick(x, y, 'left')
          print('点击挑战x=', x, 'y=', y)
          time.sleep(0.5)
          x, y, p = tt.locateImg(buzu)
          if p > 0.80:
              break;
          time.sleep(0.5)





      if num>=400:
         print('已经打了',num,'局，结束爬塔！')
         break;

      # if xunerr>=400:
      #    print('掉线，退出')
      #    break;

