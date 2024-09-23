import pyautogui
import win32gui
import time
import cv2
from liuxingIT2 import LiuXingIT2
import random
import numpy as np

if __name__ == '__main__':
  zhunbei = './daoguan/zhunbei.png'
  lvbiao = './daoguan/lvbiao.png'
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

  dishi = './zhenshe/dishi.png'
  zidong = './zhenshe/zidong.png'

  handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12-1')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
  print(h)
  tt = LiuXingIT2(h)

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
      x, y, p = tt.locateImg(zidong)
      if p > 0.80:
          tt.mouseClick(x, y, 'left')

      x, y, p = tt.locateImg(dishi)
      x1, y1, p1 = tt.locateImg(zidong)
      if p > 0.98 and p1<0.8:
          break





