import pyautogui
import win32api
import win32con
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
  sandian4 = './xinshou/sandian4.png'
  sandian5 = './xinshou/sandian5.png'
  sandian6 = './xinshou/sandian6.png'
  sandian7 = './xinshou/sandian7.png'
  sandian8 = './xinshou/sandian8.png'
  yanjing2 = './xinshou/yanjing2.png'
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
  gongji4 = './xinshou/gongji4.png'
  dao = './xinshou/dao.png'
  xue = './xinshou/xue.png'
  weizhi1 = './xinshou/weizhi1.png'
  dun3 = './xinshou/dun3.png'
  dunpai2 = './xinshou/dunpai2.png'

  zhaohuan = './xinshou/zhaohuan.png'
  lanpiao = './xinshou/lanpiao.png'
  choulan = './xinshou/choulan.png'
  queren = './xinshou/queren.png'
  chougou = './xinshou/chougou.png'
  choupu = './xinshou/choupu.png'
  choutui = './xinshou/choutui.png'
  fuli = './xinshou/fuli.png'
  jiesuo = './xinshou/jiesuo.png'

  guhuoniao = './xinshou/guhuoniao.png'
  boss = './xinshou/boss.png'
  baoxiang = './xinshou/baoxiang.png'
  tansuo = './xinshou/tansuo.png'
  fuli2 = './xinshou/fuli2.png'
  qita = './xinshou/qita.png'
  jiangli2 = './xinshou/jiangli2.png'
  tansuo4 = './xinshou/tansuo4.png'

  handle = win32gui.FindWindow('LDPlayerMainFrame', '雷电模拟器-1')
  print(handle)
  h = win32gui.FindWindowEx(handle, None, 'RenderWindow', 'TheRender')
  print(h)
  tt = LiuXingIT(h)


  #handle =  win32gui.FindWindow(None,'MuMu模拟器12-1')  #第一个参数是类目（可以不写），第二个参数名字


  def bezier(p0, p1, p2, t):
      u = 1 - t
      return u ** 2 * p0 + 2 * u * t * p1 + t ** 2 * p2

  # 起始点、控制点和结束点
  start_point = np.array([494, 340])
  control_point = np.array([766, 240])
  end_point = np.array([856, 309])

  # 生成一系列参数值
  t_values = np.linspace(0, 1, num=100)

  # 计算贝塞尔曲线上的点
  points = [bezier(start_point, control_point, end_point, t) for t in t_values]




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

      matches = tt.locateAllHuDuImg(sandian2)
      if matches:
        # 假设我们只关心最高匹配度的第一个点
        best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
        x, y = best_match[0]  # 解包坐标
        p = best_match[1]  # 匹配度
        tt.mouseClick(x, y, 'left')
        print('点击三点2', x, 'y=', y, '匹配度:', p)
        time.sleep(1)
        pass
      else:
        pass

      matches = tt.locateAllHuDuImg(sandian6)
      if matches:
            # 假设我们只关心最高匹配度的第一个点
            best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
            x, y = best_match[0]  # 解包坐标
            p = best_match[1]  # 匹配度
            tt.mouseClick(x, y, 'left')
            print('点击三点6', x, 'y=', y, '匹配度:', p)
            time.sleep(1)

      matches = tt.locateAllHuDuImg(sandian7)
      if matches:
          # 假设我们只关心最高匹配度的第一个点
          best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
          x, y = best_match[0]  # 解包坐标
          p = best_match[1]  # 匹配度
          tt.mouseClick(x, y, 'left')
          print('点击三点7', x, 'y=', y, '匹配度:', p)
          time.sleep(1)

      matches = tt.locateAllHuDuImg(sandian8)
      if matches:
          # 假设我们只关心最高匹配度的第一个点
          best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
          x, y = best_match[0]  # 解包坐标
          p = best_match[1]  # 匹配度
          tt.mouseClick(x, y, 'left')
          print('点击三点8', x, 'y=', y, '匹配度:', p)
          time.sleep(1)

      matches = tt.locateAllHuDuImg(yanjing2)
      if matches:
          # 假设我们只关心最高匹配度的第一个点
          best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
          x, y = best_match[0]  # 解包坐标
          p = best_match[1]  # 匹配度
          tt.mouseClick(x, y, 'left')
          print('点击yanjing2', x, 'y=', y, '匹配度:', p)
          time.sleep(1)

      matches = tt.locateAllHuDuImg(dunpai)
      if matches:
            # 假设我们只关心最高匹配度的第一个点
            best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
            x, y = best_match[0]  # 解包坐标
            p = best_match[1]  # 匹配度
            tt.mouseClick(x, y, 'left')
            print('点击dunpai', x, 'y=', y, '匹配度:', p)
            time.sleep(1)

      matches = tt.locateAllHuDuImg(qingming)
      if matches:
            # 假设我们只关心最高匹配度的第一个点
            best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
            x, y = best_match[0]  # 解包坐标
            p = best_match[1]  # 匹配度
            tt.mouseClick(x, y, 'left')
            print('点击清明', x, 'y=', y, '匹配度:', p)
            time.sleep(1)

      matches = tt.locateAllHuDuImg(qingming2)
      if matches:
            # 假设我们只关心最高匹配度的第一个点
            best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
            x, y = best_match[0]  # 解包坐标
            p = best_match[1]  # 匹配度
            tt.mouseClick(x, y, 'left')
            print('点击清明', x, 'y=', y, '匹配度:', p)
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

        # 点击召唤
      x, y, p = tt.locateImg(zhaohuan)
      if p > 0.90:
          tt.mouseClick(x, y, 'left')
          print('点击召唤，x=', x, 'y=', y)
          time.sleep(1)

      matches = tt.locateAllHuDuImg(zhaohuan)
      if matches:
            # 假设我们只关心最高匹配度的第一个点
            best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
            x, y = best_match[0]  # 解包坐标
            p = best_match[1]  # 匹配度
            tt.mouseClick(x, y, 'left')
            print('点击zhohuan', x, 'y=', y, '匹配度:', p)
            time.sleep(1)
            pass
      else:
            pass





        # 点击蓝票
      x, y, p = tt.locateImg(lanpiao)
      if p > 0.90:
          tt.mouseClick(x, y, 'left')
          print('点击蓝票，x=', x, 'y=', y)
          time.sleep(1)

        # 点击蓝票滑动
      x, y, p = tt.locateImg(choulan)
      if p > 0.80:
          # 定义鼠标按下和释放的消息常量
          WM_LBUTTONDOWN = 0x0201
          WM_LBUTTONUP = 0x0202

          # 遍历贝塞尔曲线上的点
          for point in points:
              x, y = int(point[0]), int(point[1])

              # 发送鼠标移动消息
              win32api.PostMessage(h, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x, y))

              # 发送鼠标左键按下消息
              win32api.PostMessage(h, WM_LBUTTONDOWN, win32con.MK_LBUTTON,
                                   win32api.MAKELONG(x, y))

              time.sleep(0.01)  # 控制每个点之间的时间间隔

          # 发送鼠标左键释放消息
          win32api.PostMessage(h, WM_LBUTTONUP, 0, 0)
          print('蓝票滑动，x=', x, 'y=', y)
          time.sleep(1)

      # 点击确认
      x, y, p = tt.locateImg(queren)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('确认', x, 'y=', y)
        time.sleep(1)

      # 点击抽勾玉
      x, y, p = tt.locateImg(chougou)
      if p > 0.85:
        tt.mouseClick(x, y, 'left')
        print('抽勾玉', x, 'y=', y)
        time.sleep(1)

      # 点击抽普通
      x, y, p = tt.locateImg(choupu)
      if p > 0.90:
        tt.mouseClick(433, 621, 'left')
        print('抽普通', 433, 'y=', 621)
        time.sleep(1)

      # 退出抽
      x, y, p = tt.locateImg(choutui)
      if p > 0.95:
        tt.mouseClick(x, y, 'left')
        print('退出抽', x, 'y=', y)
        time.sleep(1)


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



      # 雪女技能
      x, y, p = tt.locateImg(xue)
      if p > 0.80:
          tt.mouseClick(x, y, 'left')
          print('xue', x, 'y=', y)
          time.sleep(1)

      # 三点点击
      x, y, p = tt.locateImg(gongji2)
      if p > 0.50:
          tt.mouseClick(x, y, 'left')
          print('gongji2', x, 'y=', y)
          time.sleep(1)

      matches = tt.locateAllHuDuImg(gongji4)
      if matches:
            # 假设我们只关心最高匹配度的第一个点
            best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
            x, y = best_match[0]  # 解包坐标
            p = best_match[1]  # 匹配度
            tt.mouseClick(x, y, 'left')
            print('攻击', x, 'y=', y, '匹配度:', p)
            time.sleep(1)
            pass
      else:
        pass

      matches = tt.locateAllHuDuImg(sandian4)
      if matches:
            # 假设我们只关心最高匹配度的第一个点
            best_match = max(matches, key=lambda item: item[1])  # 找到匹配度最高的点
            x, y = best_match[0]  # 解包坐标
            p = best_match[1]  # 匹配度
            tt.mouseClick(x, y, 'left')
            print('三点4', x, 'y=', y, '匹配度:', p)
            time.sleep(1)
            pass
      else:
        pass



      # 刀
      x, y, p = tt.locateImg(dao)
      if p > 0.80:
          tt.mouseClick(x, y, 'left')
          print('dao', x, 'y=', y)
          time.sleep(1)

      # 刀
      x, y, p = tt.locateImg(qita)
      if p > 0.80:
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



      # 三点5
      x, y, p = tt.locateImg(sandian5)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('三点5', x, 'y=', y)
          time.sleep(1)

      # 三点5
      x, y, p = tt.locateImg(jiangli2)
      if p > 0.85:
          tt.mouseClick(1157, 251, 'left')
          print('jiangli2', x, 'y=', y)
          time.sleep(1)


      # 三点5
      x, y, p = tt.locateImg(tansuo4)
      if p > 0.85:
          tt.mouseClick(x, y, 'left')
          print('tansuo4', x, 'y=', y)
          time.sleep(1)

      # 福利退出
      x, y, p = tt.locateImg(fuli)
      if p > 0.90:
          tt.mouseClick(41, 42, 'left')
          print('福利退出')
          time.sleep(1)

      #x
      x, y, p = tt.locateImg(jiesuo)
      if p > 0.90:
          tt.mouseClick(1167, 94, 'left')
          print('jiesuo退出')
          time.sleep(1)

      #x
      x, y, p = tt.locateImg(guhuoniao)
      if p > 0.90:
          tt.mouseClick(1060, 638, 'left')
          print('1')
          time.sleep(1)

      #x
      x, y, p = tt.locateImg(boss)
      if p > 0.90:
          tt.mouseClick(x, y, 'left')
          print('boss')
          time.sleep(1)

      #x
      x, y, p = tt.locateImg(baoxiang)
      if p > 0.90:
          tt.mouseClick(x, y, 'left')
          print('baoxiang')
          time.sleep(1)

      #x
      x, y, p = tt.locateImg(tansuo)
      if p > 0.90:
          tt.mouseClick(x, y, 'left')
          print('tansuo')
          time.sleep(1)

      #x
      x, y, p = tt.locateImg(dun3)
      if p > 0.80:
          tt.mouseClick(x, y, 'left')
          print('dun')
          time.sleep(1)


      #x
      x, y, p = tt.locateImg(fuli2)
      if p > 0.80:
          tt.mouseClick(1072, 161, 'left')
          print('dun')
          time.sleep(1)





