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

  sandian = './xinshou/sandian.png'
  cv = './xinshou/cv.png'
  tiaoguo = './xinshou/tiaoguo.png'

  shushi = './xinshou/shushi.png'
  pugong = './xinshou/pugong.png'
  quanshen = './xinshou/quanshen.png'
  jixu = './xinshou/jixu.png'
  dunpai = './xinshou/dunpai.png'
  qingming = './xinshou/qingming.png'
  qingming2 = './xinshou/qingming2.png'
  wufa = './xinshou/wufa.png'
  canxue = './xinshou/canxue.png'
  sandian2 = './xinshou/sandian2.png'
  kuaijin = './xinshou/kuaijin.png'
  zhandou = './xinshou/zhandou.png'
  zhandou2 = './xinshou/zhandou2.png'
  zhandou3 = './xinshou/zhandou3.png'
  zhunbei = './xinshou/zhunbei.png'

  shoudong = './xinshou/shoudong.png'
  jiasu= './xinshou/jiasu.png'
  yanjing= './xinshou/yanjing.png'
  wenhao = './xinshou/wenhao.png'
  gongji = './xinshou/gongji.png'
  gongji2 = './xinshou/gongji2.png'
  gongji3 = './xinshou/gongji3.png'
  dao = './xinshou/dao.png'
  xue = './xinshou/xue.png'
  weizhi1 = './xinshou/weizhi1.png'
  dun3 = './xinshou/dun3.png'
  dunpai2 = './xinshou/dunpai2.png'

  img = cv2.imread('888.bmp')

  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT(h)


  #handle =  win32gui.FindWindow(None,'MuMu模拟器12-1')  #第一个参数是类目（可以不写），第二个参数名字

  while True:



      #结算1
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

      # 结算2
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



      # 三点点击
      x, y, p = tt.locateImg(dunpai)
      if p > 0.70:
          tt.mouseClick(x, y, 'left')
          print('dunpai', x, 'y=', y)
          time.sleep(1)

      # 三点点击
      x, y, p = tt.locateImg(dunpai2)
      if p > 0.70:
          tt.mouseClick(x, y, 'left')
          print('dunpai2', x, 'y=', y)
          time.sleep(1)


      # 三点点击
      x, y, p = tt.locateImg(sandian)
      if p > 0.50:
          tt.mouseClick(x, y, 'left')
          print('点击三点', x, 'y=', y)
          time.sleep(1)


       # 点击战斗
      x, y, p = tt.locateImg(zhandou)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('zhandou', x, 'y=', y)
        time.sleep(1)

       # 点击战斗
      x, y, p = tt.locateImg(zhandou2)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('zhandou2', x, 'y=', y)
        time.sleep(1)

       # 点击战斗
      x, y, p = tt.locateImg(zhandou3)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('zhandou3', x, 'y=', y)
        time.sleep(1)


      # 三点点击
      x, y, p = tt.locateImg(dun3)
      if p > 0.70:
          tt.mouseClick(x, y, 'left')
          print('dun3', x, 'y=', y)
          time.sleep(1)

      # 三点点击
      x, y, p = tt.locateImg(gongji)
      if p > 0.50:
          tt.mouseClick(x, y, 'left')
          print('gongji', x, 'y=', y)
          time.sleep(1)

      # 三点点击
      x, y, p = tt.locateImg(gongji2)
      if p > 0.50:
          tt.mouseClick(x, y, 'left')
          print('gongji2', x, 'y=', y)
          time.sleep(1)

      # 三点点击
      x, y, p = tt.locateImg(gongji3)
      if p > 0.50:
          tt.mouseClick(x, y, 'left')
          print('gongji3', x, 'y=', y)
          time.sleep(1)


      # 三点点击
      x, y, p = tt.locateImg(dao)
      if p > 0.80:
          tt.mouseClick(x, y, 'left')
          print('dao', x, 'y=', y)
          time.sleep(1)

      # 三点点击
      x, y, p = tt.locateImg(xue)
      if p > 0.80:
          tt.mouseClick(x, y, 'left')
          print('xue', x, 'y=', y)
          time.sleep(1)

      # 三点点击
      x, y, p = tt.locateImg(weizhi1)
      if p > 0.80:
          tt.mouseClick(x, y, 'left')
          print('xue', x, 'y=', y)
          time.sleep(1)

        # cv点击
      x, y, p = tt.locateImg(cv)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击cv', x, 'y=', y)
          time.sleep(1)

        # 遇到基础术士
      x, y, p = tt.locateImg(shushi)
      if p > 0.85:
          x, y, p = tt.locateImg(pugong)
          if p > 0.85:
           tt.mouseClick(x, y, 'left')
           print('点击普攻', x, 'y=', y)
           time.sleep(1)

        # 点击犬神
      x, y, p = tt.locateImg(quanshen)
      if p > 0.70:
          tt.mouseClick(x, y, 'left')
          print('点击犬神', x, 'y=', y)
          time.sleep(1)

        # 点击继续
      x, y, p = tt.locateImg(jixu)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击继续', x, 'y=', y)
          time.sleep(1)

        # 点击盾牌
      x, y, p = tt.locateImg(dunpai)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击盾牌', x, 'y=', y)
          time.sleep(1)

        # 点击清明
      x, y, p = tt.locateImg(qingming)
      if p > 0.70:
          tt.mouseClick(x, y, 'left')
          print('点击清明', x, 'y=', y)
          time.sleep(1)

          # 点击普攻
      x, y, p = tt.locateImg(wufa)
      if p > 0.85:
          x, y, p = tt.locateImg(pugong)
          if p > 0.85:
              tt.mouseClick(x, y, 'left')
              print('点击普攻', x, 'y=', y)
              time.sleep(1)

     # 点击残血
      x, y, p = tt.locateImg(canxue)
      if p > 0.70:
        tt.mouseClick(x, y, 'left')
        print('点击残血犬神', x, 'y=', y)
        time.sleep(1)



     # 点击三点2
      x, y, p = tt.locateImg(sandian2)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('点击sandian2', x, 'y=', y)
        time.sleep(1)

        # 点击清明2
      x, y, p = tt.locateImg(qingming2)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击清明2', x, 'y=', y)
          time.sleep(1)

      # 点击跳过
      x, y, p = tt.locateImg(tiaoguo)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击跳过', x, 'y=', y)
          time.sleep(1)

      # 点击准备
      x, y, p = tt.locateImg(zhunbei)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击准备', x, 'y=', y)
          time.sleep(1)

      # 点击手动
      x, y, p = tt.locateImg(shoudong)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击手动', x, 'y=', y)
          time.sleep(1)

      # 点击加速
      x, y, p = tt.locateImg(jiasu)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击加速', x, 'y=', y)
          time.sleep(1)

      # 点击眼镜
      x, y, p = tt.locateImg(yanjing)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击眼镜', x, 'y=', y)
          time.sleep(1)

      # 点击问号
      x, y, p = tt.locateImg(wenhao)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击眼镜', x, 'y=', y)
          time.sleep(1)



     # 点击快进
      x, y, p = tt.locateImg(kuaijin)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('点击sandian2', x, 'y=', y)
        time.sleep(1)

       # 点击战斗
      x, y, p = tt.locateImg(zhandou)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('点击sandian2', x, 'y=', y)
        time.sleep(1)

      # 点击战斗
      x, y, p = tt.locateImg(zhandou2)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('zhandou2', x, 'y=', y)
          time.sleep(1)

      # 点击战斗
      x, y, p = tt.locateImg(zhandou3)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('zhandou3', x, 'y=', y)
          time.sleep(1)





