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

  dabuguo = './jiesuan/dabuguo.png'
  zhunbei = './jiesuan/zhunbei.png'
  fanhui = './jiesuan/fanhui.png'
  queren = './jiesuan/queren.png'
  queding = './jiesuan/queding.png'
  shuaxin = './jiesuan/shuaxin.png'
  tupoyemian = './jiesuan/tupoyemian.png'
  po = './jiesuan/po.png'
  qiguai = './jiesuan/qiguai.png'
  buzu = './jiesuan/buzu.png'
  buzu2 = './jiesuan/buzu2.png'

  #悬赏
  xuanshang = './huodong/xuanshang.png'
  gouxie = './huodong/gouxie.png'
  jieshou = './huodong/jieshou.png'
  jujue = './huodong/jujue.png'


  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT(h)

  # 定义生成随机坐标的函数
  # 定义生成随机坐标的函数
  def generate_random_coordinates(mu_x, sigma_x, range_x, mu_y, sigma_y, range_y):
    x = np.random.normal(mu_x, sigma_x)
    y = np.random.normal(mu_y, sigma_y)

    # 确保生成的坐标在指定范围内
    while x < range_x[0] or x > range_x[1]:
      x = np.random.normal(mu_x, sigma_x)
    while y < range_y[0] or y > range_y[1]:
      y = np.random.normal(mu_y, sigma_y)

    return x, y


  # 定义鼠标点击函数
  def mouse_click(x, y):
    tt.mouseClick(x, y, 'left')
    print(f'点击坐标 x={x}, y={y}')
    time.sleep(1)


  # 定义检查图片函数
  def check_image(images):
    for image in images:
      x, y, p = tt.locateImg(image)
      if p > 0.85:
        return x, y
    return None, None


  # 需要正态分布点击的图片列表
  settlement_images = [jiesuan1, jiesuan2,diancuo,qiguai]
  # 定义突破状态变量
  tupo_state = 0
  # 定义失败次数
  failed = 0
  turefaile = 0

  flag = False


  while True:

    #查找有多少个失败，鸡肋，不太准
    if not flag:
      list = tt.locateAllImg(dabuguo)
      print(list)
      failed = len(list)
      flag = True

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
      failed = failed + 1
      time.sleep(1)


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

    # 检查结算图片
    x, y = check_image(settlement_images)
    if x is not None and y is not None:
      x, y = generate_random_coordinates(1200, 30, (1144, 1256), 437, 100, (185, 689))
      mouse_click(x, y)

    # x, y, p = tt.locateImg(buzu)
    # if p > 0.99:
    #   print('个突完毕')
    #   break



    x, y, p = tt.locateImg(zhunbei)
    if p > 0.85:
      x = random.randint(x - 30, x + 30)
      y = random.randint(y - 15, y + 15)
      mouse_click(x, y)
      print('点击准备')

    x, y, p = tt.locateImg(jingong)
    if p > 0.85:
      x = random.randint(x - 30, x + 30)
      y = random.randint(y - 15, y + 15)
      mouse_click(x, y)
      print('点击进攻')
      # 识别突破券不足
      x, y, p = tt.locateImg(buzu2)
      if p > 0.98:
        print('突破券不足')
        break
      x, y, p = tt.locateImg(buzu)
      if p > 0.80:
        break

    x, y, p = tt.locateImg(buzu2)
    if p > 0.98:
      print('突破券不足')
      break


    x, y, p = tt.locateImg(buzu)
    if p > 0.80:
      break

    x, y, p2 = tt.locateImg(queding)
    if p2 > 0.85:
      x = random.randint(x - 15, x + 15)
      y = random.randint(y - 5, y + 5)
      mouse_click(x, y)
      print('点击确定')

    x, y, p3 = tt.locateImg(qiguai)
    x, y, p = tt.locateImg(tupoyemian)
    if p > 0.85 and p2 <0.85 and p3 <0.8:
       print('处于突破页面')
       # 第一个突破标志
       if tupo_state == 0:
         turefaile = 0
         x, y, p = tt.locateImg(tupotu, region=(139, 139, 473, 273))
         if p > 0.85:
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破1标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(139, 139, 473, 273))
           if p > 0.95:
             # print('突破1开始failed =', failed)
             # failed = failed + 1
             print('突破1后failed =', failed)
             tupo_state = 1
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(139, 139, 473, 273))
           # if p > 0.80:
             print('突破1成功,failed =',failed)
             tupo_state = 1

       # 第二个突破标志
       elif tupo_state == 1:
         x, y, p = tt.locateImg(tupotu, region=(473, 139, 804, 273))
         if p > 0.85:
           print('识别突破2', x, y)
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破2标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(473, 139, 804, 273))
           if p > 0.95:
             # print('突破2开始failed =', failed)
             # failed = failed + 1
             print('突破2后failed =', failed)
             tupo_state = 2
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(473, 139, 804, 273))
           # if p > 0.80:
             print('突破2成功,failed =',failed)
             tupo_state = 2

       # 第三个突破标志
       elif tupo_state == 2:
         x, y, p = tt.locateImg(tupotu, region=(807, 139, 1140, 273))
         if p > 0.85:
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破3标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(807, 139, 1140, 273))
           if p > 0.95:
             print('3',x,y,p)
             # print('突破3开始failed =',failed)
             # failed = failed + 1
             print('突破3失败,failed =',failed)
             tupo_state = 3
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(807, 139, 1140, 273))
           # if p > 0.80:
             print('突破3成功,failed =',failed)
             tupo_state = 3

       # 第四个突破标志
       elif tupo_state == 3:
         x, y, p = tt.locateImg(tupotu, region=(139, 279, 473, 404))
         if p > 0.85:
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破4标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(139, 279, 473, 404))
           if p > 0.95:
             # print('突破4开始failed =', failed)
             # failed = failed + 1
             print('突破4后failed =', failed)
             tupo_state = 4
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(139, 279, 473, 404))
           # if p > 0.80:
             print('突破4成功,failed =',failed)
             tupo_state = 4

       # 第五个突破标志
       elif tupo_state == 4:
         x, y, p = tt.locateImg(tupotu, region=(473, 279, 804, 404))
         if p > 0.85:
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破5标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(473, 279, 804, 404))
           if p > 0.95:
             # print('突破5开始failed =', failed)
             # failed = failed + 1
             print('突破5后failed =', failed)
             tupo_state = 5
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(473, 279, 804, 404))
           # if p > 0.80:
             print('突破5成功,failed =',failed)
             tupo_state = 5

       # 第六个突破标志
       elif tupo_state == 5:
         x, y, p = tt.locateImg(tupotu, region=(807, 279, 1140, 404))
         if p > 0.85:
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破6标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(807, 279, 1140, 404))
           if p > 0.95:
             print('6失败', x, y, p)
             # print('突破6开始failed =', failed)
             # failed = failed + 1
             print('突破6失败,failed =',failed)
             tupo_state = 6
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(807, 279, 1140, 404))
           # if p > 0.80:
             print('突破6成功,failed =',failed)
             tupo_state = 6

       # 第七个突破标志
       elif tupo_state == 6:
         x, y, p = tt.locateImg(tupotu, region=(139, 412, 473, 543))
         if p > 0.85:
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破7标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(139, 412, 473, 543))
           if p > 0.95:
             # print('突破7开始failed =', failed)
             # failed = failed + 1
             print('突破7后failed =', failed)
             tupo_state = 7
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(139, 412, 473, 543))
           # if p > 0.80:
             print('突破7成功,failed =',failed)
             tupo_state = 7

       # 第8个突破标志
       elif tupo_state == 7:
         x, y, p = tt.locateImg(tupotu, region=(473, 412, 804, 543))
         if p > 0.85:
           x = random.randint(x - 180, x)
           y = random.randint(y + 10, y + 80)
           mouse_click(x, y)
           print('识别突破8标志')
         else:
           x, y, p = tt.locateImg(dabuguo, region=(473, 412, 804, 543))
           if p > 0.95:
             # print('突破8开始failed =', failed)
             # failed = failed + 1
             print('突破8后failed =', failed)
             tupo_state = 8
             time.sleep(1)
           else:
           # x, y, p = tt.locateImg(po, region=(473, 412, 804, 543))
           # if p > 0.80:
             print('突破8成功,failed =',failed)
             tupo_state = 8


       # 第9个突破标志
       elif tupo_state == 8:
         print('failed=', failed)
         if failed <= 4:
           failedNum = 4 - failed
           x, y, p = tt.locateImg(tupotu, region=(807, 412, 1140, 543))
           if p > 0.85:
             x = random.randint(x - 180, x)
             y = random.randint(y + 10, y + 80)
             mouse_click(x, y)
             print('识别突破9标志,还需要失败', failedNum)
           while True:

               x, y = check_image(settlement_images)
               if x is not None and y is not None:
                 x, y = generate_random_coordinates(1200, 30, (1144, 1256), 437, 100, (185, 689))
                 mouse_click(x, y)

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
                 failed = failed + 1
                 print(failed)
                 time.sleep(1)

               x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
               if p > 0.95:
                 print('突破9失败')
                 x = random.randint(x - 180, x)
                 y = random.randint(y + 10, y + 80)
                 mouse_click(x, y)

               x, y, p = tt.locateImg(jingong)
               if p > 0.85:
                 x = random.randint(x - 30, x + 30)
                 y = random.randint(y - 15, y + 15)
                 mouse_click(x, y)
                 print('点击进攻')
                 # 识别突破券不足
                 x, y, p = tt.locateImg(buzu)
                 if p > 0.80:
                   break



               x, y, p = tt.locateImg(fanhui)
               if p > 0.85:
                 x = random.randint(x - 5, x + 5)
                 y = random.randint(y - 5, y + 5)
                 mouse_click(x, y)

               x, y, p = tt.locateImg(queren)
               if p > 0.85:
                 x = random.randint(x - 15, x + 15)
                 y = random.randint(y - 5, y + 5)
                 mouse_click(x, y)
                 time.sleep(1.5)

               if failed >= 4:
                 break

         else:
           print('没到9就失败那么多次')
           turefaile == 0
           x, y, p = tt.locateImg(tupotu, region=(807, 412, 1140, 543))
           if p > 0.85:
             x = random.randint(x - 180, x)
             y = random.randint(y + 10, y + 80)
             mouse_click(x, y)
             print('识别突破9标志')
           pass

       #最后一次突破9
       x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
       if p > 0.95 and turefaile == 0:
         print('突破9且从来没真打过')
         x = random.randint(x - 180, x)
         y = random.randint(y + 10, y + 80)
         mouse_click(x, y)
         turefaile = 1
         failed = 0
       time.sleep(1)


       x, y, p = tt.locateImg(jingong)
       if p > 0.85:
         time.sleep(1)
         x = random.randint(x - 30, x + 30)
         y = random.randint(y - 15, y + 15)
         mouse_click(x, y)
         print('点击进攻')
         # 识别突破券不足
         x, y, p = tt.locateImg(buzu)
         if p > 0.80:
           break

       x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
       if p > 0.95 and turefaile == 1:
         print('真失败了')
         tupo_state = 0
         failed = 0
         x, y, p = tt.locateImg(shuaxin)
         if p > 0.85:
           x = random.randint(x - 15, x + 15)
           y = random.randint(y - 5, y + 5)
           # time.sleep(200)
           mouse_click(x, y)
           turefaile = 0

       # x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
       # if p < 0.95 and turefaile == 1:
       #   print('打了突破9，进行新一轮')
       #   tupo_state = 0
       #   failed = 0
       #   turefaile = 0


       x, y, p = tt.locateImg(po, region=(807, 412, 1140, 543))
       if p > 0.80:
         print('突破9成功')
         x, y, p = tt.locateImg(shuaxin)
         if p > 0.80:
           x = random.randint(x - 15, x + 15)
           y = random.randint(y - 5, y + 5)
           # time.sleep(200)
           mouse_click(x, y)
           tupo_state = 0
           failed = 0
           turefaile = 0
         else:
           print('找不到刷新')

       # x, y, p = tt.locateImg(shuaxin)
       # if p > 0.85 and turefaile == 1:
       #   x = random.randint(x - 15, x + 15)
       #   y = random.randint(y - 5, y + 5)
       #   # time.sleep(200)
       #   mouse_click(x, y)
       #   turefaile = 0







