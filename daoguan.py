import pyautogui
import win32gui
import time
import cv2
from liuxingIT import LiuXingIT
import random

if __name__ == '__main__':
  zhunbei = './daoguan/zhunbei.png'
  lvbiao = './daoguan/lvbiao.png'
  tianzhao = './daoguan/tianzhao.png'
  img = cv2.imread('888.bmp')

  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT(h)


  handle =  win32gui.FindWindow(None,'MuMu模拟器12')  #第一个参数是类目（可以不写），第二个参数名字
  while True:
      x, y, p = tt.locateImg(zhunbei)
      if p > 0.85:
          time.sleep(1)
          while True:
              tt.shot()
              rgb = img[560, 1222][::-1]  # 获取指定点的像素值 第一个10是y
              print('rgb',rgb)
              if rgb[0] >= 100 and rgb[1] >= 100 and rgb[2] >= 100:
                  x = random.randint(1134, 1221)
                  y = random.randint(562, 613)
                  tt.mouseClick(x, y, 'left')
                  print('点击准备')
                  time.sleep(1.5)
                  break
              else:
                  print('匹配不到这个像素点')

          x, y, p = tt.locateImg(lvbiao)
          if p > 0.85:
              print('找到绿标')
          else:
              print('没有找到绿标')
              while True:
                  x, y, p = tt.locateImg(tianzhao)  # region=(127, 260, 1208, 584)
                  if p > 0.85:
                          x = random.randint(x - 2, x + 3)
                          y = random.randint(y - 2, y + 3)
                          tt.mouseClick(x, y, 'left')
                          print('点击天照完毕')
                          break
      else:
          pass




