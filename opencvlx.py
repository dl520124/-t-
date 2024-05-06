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
  sandian3 = './xinshou/sandian3.png'
  kuaijin = './xinshou/kuaijin.png'
  zhandou = './xinshou/zhandou.png'
  zhandou2 = './xinshou/zhandou2.png'
  zhandou3 = './xinshou/zhandou3.png'
  zhunbei = './xinshou/zhunbei.png'

  shoudong = './xinshou/shoudong.png'
  jiasu = './xinshou/jiasu.png'
  yanjing = './xinshou/yanjing.png'
  wenhao = './xinshou/wenhao.png'
  gongji = './xinshou/gongji.png'
  gongji2 = './xinshou/gongji2.png'
  gongji3 = './xinshou/gongji3.png'
  dao = './xinshou/dao.png'
  xue = './xinshou/xue.png'
  weizhi1 = './xinshou/weizhi1.png'
  dun3 = './xinshou/dun3.png'
  dunpai2 = './xinshou/dunpai2.png'

  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT(h)



  while True:
      # 结算1
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

      matches = tt.locateAllHuDuImg(sandian3)

      if matches:
        # 假设我们只关心最高匹配度的第一个点
        best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
        x, y = best_match[0]  # 解包坐标
        p = best_match[1]  # 匹配度
        tt.mouseClick(x, y, 'left')
        print('点击三点3', x, 'y=', y, '匹配度:', p)
        time.sleep(1)
        pass
      else:
        pass

      # 点击战斗
      x, y, p = tt.locateImg(zhandou)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('zhandou', x, 'y=', y)
        time.sleep(1)


      # 点击问号
      x, y, p = tt.locateImg(wenhao)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击眼镜', x, 'y=', y)
          time.sleep(1)

      # 点击眼镜
      x, y, p = tt.locateImg(yanjing)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击眼镜', x, 'y=', y)
          time.sleep(1)


      # 点击准备
      x, y, p = tt.locateImg(zhunbei)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击准备', x, 'y=', y)
          time.sleep(1)

      # 点击跳过
      x, y, p = tt.locateImg(tiaoguo)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击跳过', x, 'y=', y)
          time.sleep(1)


        # 点击继续
      x, y, p = tt.locateImg(jixu)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击继续', x, 'y=', y)
          time.sleep(1)


        # cv点击
      x, y, p = tt.locateImg(cv)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('点击cv', x, 'y=', y)
          time.sleep(1)

          # 点击快进
      x, y, p = tt.locateImg(kuaijin)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('点击sandian2', x, 'y=', y)
        time.sleep(1)




























  # import cv2  # 导入库
  #
  # img = cv2.imread("1.bmp")  # 读取图片
  # # img.shape  # 读取图片的形状(width，height，channel)
  # # img_dtype = img.dtype  # 图片的数据类型
  # # (b,g,r) = img[6,40]  #获取图片坐标系的bgr色
  # # print(b,g,r)
  #
  # img1 = cv2.imread("./ceshi/1.bmp")  # 读取图片
  # # 转换成灰度图
  # gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  #
  # # 显示灰度图
  # cv2.imshow('Gray image', gray_image)
  # cv2.waitKey(0) #等待，必要的步骤，不然一闪而过
  # cv2.destroyAllWindows()#关闭所以的窗口


  #
  #
  # b = img[6,40,0]    #BGR 0为通道 蓝色
  # g = img[6,40,1]  #BGR 1为通道 绿色
  # r = img[6,40,2]  #BGR 2为通道 红色
  #
  # #重新给像素赋值，更换颜色
  # img[6,40]=(0,0,255)
  #
  # cv2.imshow("图片名字",img)
  # cv2.waitKey(0) #等待，必要的步骤，不然一闪而过
  # cv2.destroyAllWindows()#关闭所以的窗口
  #
  # img2 = cv2.imread("huidu.jpg",cv2.IMREAD_GRAYSCALE)  #读取灰度图片
  #
  # cv2.imshow("huidu",img2)
  # cv2.waitKey(0) #等待，必要的步骤，不然一闪而过
  # cv2.destroyAllWindows()#关闭所以的窗口


  # logo = cv2.imread("1.bmp")
  # b,g,r = cv2.split(logo)  # 获取整张图片的b，g，r
  # img_new = cv2.merge([r,g,b])  # 调整b，g，r的顺序
  # import matplotlib.pyplot as plt
  #
  # plt.subplot(121)
  # plt.imshow(logo)
  # plt.subplot(122)
  # plt.imshow(img_new)
  # plt.show()
