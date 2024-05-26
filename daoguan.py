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

  def mouse_click(x, y):
    tt.mouseClick(x, y, 'left')
    print(f'点击坐标 x={x}, y={y}')
    time.sleep(1)

  while True:
      x, y, p = tt.locateImg(zhunbei)
      if p > 0.85:
          x = random.randint(x - 30, x + 30)
          y = random.randint(y - 15, y + 15)
          mouse_click(x, y)
          print('点击准备')





