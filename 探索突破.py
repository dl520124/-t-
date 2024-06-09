import numpy as np
import pyautogui
import win32api
import win32con
import win32gui
import win32ui
from liuxingIT import LiuXingIT
import liuxingIT
import time
import random

# 这里可以使用 liuxingIT 模块中的函数和类


if __name__ == '__main__':

    def bezier(p0, p1, p2, t):
        u = 1 - t
        return u ** 2 * p0 + 2 * u * t * p1 + t ** 2 * p2

    xiaoguai = './tansuo/xiaoguai.png'
    boss = './tansuo/boss.png'
    jiesuan1 = './tansuo/jiesuan1.png'
    jiesuan2 = './tansuo/jiesuan2.png'
    neibaoxiang = './tansuo/neibaoxiang.png'
    queren = './tansuo/queren.png'
    k28 = './tansuo/k28.png'
    k2 = './tansuo/k2.png'
    k4 = './tansuo/k4.png'
    k5 = './tansuo/k5.png'
    k7 = './tansuo/k7.png'
    k9 = './tansuo/k9.png'
    k10 = './tansuo/k10.png'
    k17 = './tansuo/k17.png'
    tansuo = './tansuo/tansuo.png'

    yingbing = './tansuo/yingbing.png'

    # 悬赏
    xuanshang = './huodong/xuanshang.png'
    gouxie = './huodong/gouxie.png'
    jieshou = './huodong/jieshou.png'
    jujue = './huodong/jujue.png'

    yao = './tansuo/yao.png'
    weizhi1 = './tansuo/weizhi1.png'
    waibaoxiang = './tansuo/waibaoxiang.png'
    waibaoxiang2 = './tansuo/waibaoxiang2.png'
    tuichu = './tansuo/tuichu.png'
    tili = './tansuo/tili.png'
    ji57 = './jiesuan/57ji.png'
    buzu3 = './jiesuan/buzu3.png'

    #突破
    tupotu = './jiesuan/tupotu.png'
    jingong = './jiesuan/jingong.png'
    wancheng = './jiesuan/wancheng.png'
    shibai = './jiesuan/shibai.png'
    diancuo = './jiesuan/diancuo.png'

    dabuguo = './jiesuan/dabuguo.png'
    zhunbei = './jiesuan/zhunbei.png'
    fanhui = './jiesuan/fanhui.png'
    queding = './jiesuan/queding.png'
    shuaxin = './jiesuan/shuaxin.png'
    tupoyemian = './jiesuan/tupoyemian.png'
    po = './jiesuan/po.png'
    qiguai = './jiesuan/qiguai.png'
    buzu = './jiesuan/buzu.png'
    buzu2 = './jiesuan/buzu2.png'
    diantupo = './jiesuan/diantupo.png'


    #未完成，还是要识别字，不然容易错误

    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT(h)
    number = 0;
    baonum =0;
    sainum = 0;
    bossStop = 0;
    tansuo_state = 0

    #突破用的
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
        # time.sleep(1)

        # 定义检查图片函数


    def check_image(images):
        for image in images:
            x, y, p = tt.locateImg(image)
            if p > 0.85:
                return x, y
        return None, None

        # 需要正态分布点击的图片列表


    settlement_images = [jiesuan1, jiesuan2, diancuo, qiguai]
    # 定义突破状态变量
    tupo_state = 0
    # 定义失败次数
    failed = 0
    turefaile = 0
    last_refresh_time = 0
    shuaxinone = 0

    flag = False


    #打多少次小怪转突破
    fitguainum = 72

    while True:
      if tansuo_state == 0: #探索状态
        # time.sleep(1)
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
        x, y, p = tt.locateImg(yingbing, None)
        if p > 0.85:
            print('探索里面')
            time.sleep(0.5)
            x, y, p = tt.locateImg(boss, None)
            if p < 0.80:
                x, y, p = tt.locateImg(xiaoguai, None)
                if p > 0.80:
                    x = random.randint(x - 15, x + 15)
                    y = random.randint(y - 15, y + 15)
                    tt.mouseClick(x, y, 'left')
                    print('找到小怪,点击了:', x, y)
                    sainum = 0;
                else:
                    # time.sleep(2)
                    x, y, p = tt.locateImg(neibaoxiang, None)
                    if p > 0.80:
                        print('有内宝箱')
                        # time.sleep(1)
                        x, y, p = tt.locateImg(queren, None)
                        time.sleep(0.5)
                        if p < 0.85 :
                            x = random.randint(40, 75)
                            y = random.randint(40, 75)
                            tt.mouseClick(x, y)
                            print('点击返回')
                        # time.sleep(1.5)
                        x, y, p = tt.locateImg(queren, None)
                        if p > 0.85:
                            x = random.randint(718, 835)
                            y = random.randint(390, 420)
                            tt.mouseClick(x, y)
                            print('点击确认')
                    else:
                        # time.sleep(1.5)
                        x, y, p = tt.locateImg(queren, None)
                        if p > 0.85:
                            x = random.randint(718, 835)
                            y = random.randint(390, 420)
                            tt.mouseClick(x, y)
                            print('点击确认')
                        x, y, p = tt.locateImg(yingbing, None)
                        if p > 0.85:
                            print('没有内宝箱也找不到小怪且在探索画面')
                            x, y, p = tt.locateImg(weizhi1, None)
                            print('bossStop',bossStop)
                            if p < 0.85 and bossStop == 0:
                                # 起始点、控制点和结束点
                                x1 = random.randint(1000, 1200)
                                y1 = random.randint(150, 180)

                                x2 = random.randint(600, 800)
                                y2 = random.randint(200, 400)

                                x3 = random.randint(200, 400)
                                y3 = random.randint(100, 300)
                                print('起始坐标', x1, y1)
                                print('控制坐标', x2, y2)
                                print('结束坐标', x3, y3)

                                start_point = np.array([x1, y1])
                                control_point = np.array([x2, y2])
                                end_point = np.array([x3, y3])

                                # 生成一系列参数值
                                num = random.randint(10, 50)
                                t_values = np.linspace(0, 1, num=num)
                                print('贝塞尔num', num)

                                # 计算贝塞尔曲线上的点
                                points = [bezier(start_point, control_point, end_point, t) for t in t_values]

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
                                    time.sleep(random.uniform(0.01, 0.03))  # 控制每个点之间的时间间隔
                                # 发送鼠标左键释放消息
                                win32api.PostMessage(h, WM_LBUTTONUP, 0, 0)
                                # time.sleep(1)
                                sainum = sainum + 1;

                                if sainum >= 2:
                                    print('滑动超过3次，退出')
                                    x = random.randint(40, 75)
                                    y = random.randint(40, 75)
                                    tt.mouseClick(x, y)
                                    print('点击返回')
                                    # time.sleep(1.5)
                                    x, y, p = tt.locateImg(queren, None)
                                    if p > 0.85:
                                        x = random.randint(718, 835)
                                        y = random.randint(390, 420)
                                        tt.mouseClick(x, y)
                                        print('点击确认')

                            if p > 0.85:
                                print('识别未知1')
                                x = random.randint(40, 75)
                                y = random.randint(40, 75)
                                tt.mouseClick(x, y)
                                print('点击返回')
            else:
                x = random.randint(x - 15, x + 15)
                y = random.randint(y - 15, y + 15)
                tt.mouseClick(x, y, 'left')
                print('找到boss,点击了:', x, y)
                bossStop = 1;

            x, y, p = tt.locateImg(queren, None)
            if p > 0.85:
                x = random.randint(718, 835)
                y = random.randint(390, 420)
                tt.mouseClick(x, y)
                print('点击确认')

            x, y, p = tt.locateImg(tili)
            if p > 0.85:
                print('体力不足')
                break


        else:
            # print('找不到樱饼')
            pass




        x, y, p = tt.locateImg(jiesuan1)
        if p > 0.80:
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
            # time.sleep(1)
            number = number + 1;
            print('number=', number);

        x, y, p = tt.locateImg(jiesuan2)
        if p > 0.85:
            # time.sleep(1)
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
            # time.sleep(1)

        x, y, p = tt.locateImg(yao, region=(400, 4, 467, 73))
        if p > 0.85:
            bossStop = 0; #初始化boss滑动
            # time.sleep(1)
            print('已经点击',baonum,'次宝箱')
            print('不是探索页面')
            x, y, p = tt.locateImg(waibaoxiang2, None)
            if p > 0.85:
                print('有宝箱')
                x, y, p = tt.locateImg(tuichu, None)
                if p > 0.85:
                    print('有退出按钮')
                    tt.mouseClick(x, y)
                else:
                    x, y, p = tt.locateImg(waibaoxiang2, None)
                    if p > 0.85:
                        tt.mouseClick(x, y)
                        baonum = baonum + 1
                        print('已经点击',baonum,'次宝箱')
            else:
                print('没有宝箱')
                if number >=fitguainum:
                    print('打够',number,'次小怪了')
                    x, y, p = tt.locateImg(tuichu)
                    print(p, '退出')
                    if p > 0.85:
                        tt.mouseClick(x, y)
                    else:
                        x, y, p = tt.locateImg(diantupo)
                        if p > 0.85:
                            tt.mouseClick(x, y)
                            tansuo_state = 1  # 进入突破状态
                    x, y, p = tt.locateImg(diantupo)
                    if p > 0.85:
                        tt.mouseClick(x, y)
                        number = 0
                        tansuo_state = 1  # 进入突破状态
                x, y, p = tt.locateImg(tansuo, region=(863, 500, 1020, 576))
                print("判断探索")
                if p > 0.85 and number<fitguainum and tansuo_state == 0:
                    x = random.randint(900, 986)
                    y = random.randint(523, 553)
                    tt.mouseClick(x, y)
                else:
                    pass

                x, y, p = tt.locateImg(k28, region=(1000,120,1270,700))
                print('判断K28，已打小怪次数',number)
                if p > 0.80 and number<fitguainum and tansuo_state == 0:
                    x = random.randint(x - 53, x + 88)
                    y = random.randint(y, y + 79)
                    tt.mouseClick(x, y)
                    bossStop = 0;
                else:
                    #print('找不到k2')
                    pass
        x, y, p = tt.locateImg(weizhi1, None)
        if p > 0.85:
            print('外识别未知1')
            x = random.randint(40, 75)
            y = random.randint(40, 75)
            tt.mouseClick(x, y)
            print('点击返回')

        x, y, p = tt.locateImg(ji57)
        if p > 0.95:
            print("已经57级")
            break





        # if number>=100:
        #     break
      if tansuo_state == 1:  # 突破状态
          time.sleep(1)
          # 查找有多少个失败，鸡肋，不太准
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
              # time.sleep(1)

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

          x, y, p = tt.locateImg(buzu2)
          if p > 0.98:
              print('突破券不足')
              x, y, p = tt.locateImg(tuichu)
              if p > 0.85:
                  tt.mouseClick(x, y)
                  tansuo_state = 0

          x, y, p2 = tt.locateImg(queding)
          if p2 > 0.85:
              x = random.randint(x - 15, x + 15)
              y = random.randint(y - 5, y + 5)
              mouse_click(x, y)
              print('点击确定')
              turefaile = 0
              tupo_state = 0
              failed = 0
              shuaxinone = 0

          x, y, p3 = tt.locateImg(qiguai)
          x, y, p = tt.locateImg(tupoyemian)
          if p > 0.85 and p2 < 0.85 and p3 < 0.8:
              print('处于突破页面')
              # 第一个突破标志
              if tupo_state == 0:
                  last_refresh_time = time.time()
                  turefaile = 0
                  x, y, p = tt.locateImg(shuaxin)
                  if p > 0.9:
                      shuaxinone = 1  # 刷新未冷却
                      print('刷新未冷却')
                  x, y, p = tt.locateImg(tupotu, region=(139, 139, 473, 273))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破1标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(139, 139, 473, 273))
                      if p > 0.95:
                          print('突破1后failed =', failed)
                          tupo_state = 1
                      else:
                          print('突破1成功,failed =', failed)
                          tupo_state = 1

              # 第二个突破标志
              elif tupo_state == 1:
                  x, y, p = tt.locateImg(tupotu, region=(473, 139, 804, 273))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      print('识别突破2', x, y)
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破2标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(473, 139, 804, 273))
                      if p > 0.95:
                          print('突破2后failed =', failed)
                          tupo_state = 2
                      else:
                          print('突破2成功,failed =', failed)
                          tupo_state = 2

              # 第三个突破标志
              elif tupo_state == 2:
                  x, y, p = tt.locateImg(tupotu, region=(807, 139, 1140, 273))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破3标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(807, 139, 1140, 273))
                      if p > 0.95:
                          print('3', x, y, p)
                          print('突破3失败,failed =', failed)
                          tupo_state = 3
                          # time.sleep(1)
                      else:
                          print('突破3成功,failed =', failed)
                          tupo_state = 3

              # 第四个突破标志
              elif tupo_state == 3:
                  x, y, p = tt.locateImg(tupotu, region=(139, 279, 473, 404))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破4标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(139, 279, 473, 404))
                      if p > 0.95:
                          print('突破4后failed =', failed)
                          tupo_state = 4
                      else:
                          print('突破4成功,failed =', failed)
                          tupo_state = 4

              # 第五个突破标志
              elif tupo_state == 4:
                  x, y, p = tt.locateImg(tupotu, region=(473, 279, 804, 404))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破5标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(473, 279, 804, 404))
                      if p > 0.95:
                          print('突破5后failed =', failed)
                          tupo_state = 5
                      else:
                          print('突破5成功,failed =', failed)
                          tupo_state = 5

              # 第六个突破标志
              elif tupo_state == 5:
                  x, y, p = tt.locateImg(tupotu, region=(807, 279, 1140, 404))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破6标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(807, 279, 1140, 404))
                      x2, y2, p2 = tt.locateImg(jingong)
                      if p > 0.85 and p2 < 0.85:
                          print('6失败', x, y, p)
                          print('突破6失败,failed =', failed)
                          tupo_state = 6
                      else:
                          print('突破6成功,failed =', failed)
                          tupo_state = 6

              # 第七个突破标志
              elif tupo_state == 6:
                  x, y, p = tt.locateImg(tupotu, region=(139, 412, 473, 543))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破7标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(139, 412, 473, 543))
                      if p > 0.95:
                          print('突破7后failed =', failed)
                          tupo_state = 7
                      else:
                          print('突破7成功,failed =', failed)
                          tupo_state = 7

              # 第8个突破标志
              elif tupo_state == 7:
                  x, y, p = tt.locateImg(tupotu, region=(473, 412, 804, 543))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      x = random.randint(x - 180, x)
                      y = random.randint(y + 10, y + 80)
                      mouse_click(x, y)
                      print('识别突破8标志')
                  else:
                      x, y, p = tt.locateImg(dabuguo, region=(473, 412, 804, 543))
                      if p > 0.95:
                          print('突破8后failed =', failed)
                          tupo_state = 8
                      else:
                          print('突破8成功,failed =', failed)
                          tupo_state = 8


              # 第9个突破标志
              elif tupo_state == 8:
                  print('failed=', failed)
                  if failed <= 4:
                      failedNum = 4 - failed
                      x, y, p = tt.locateImg(tupotu, region=(807, 412, 1140, 543))
                      x2, y2, p2 = tt.locateImg(jingong)
                      if p > 0.85 and p2 < 0.85:
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

                          if failed >= 4:
                              x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
                              x2, y2, p2 = tt.locateImg(jingong)
                              if p > 0.85 and p2 < 0.85:
                                  x = random.randint(x - 180, x)
                                  y = random.randint(y + 10, y + 80)
                                  mouse_click(x, y)
                                  print('识别突破9标志，打了一次')
                                  turefaile = 1  # 打过一次9了
                                  tupo_state = 9
                                  break

                          x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
                          x2, y2, p2 = tt.locateImg(jingong)
                          if p > 0.85 and p2 < 0.85 and failed < 4:
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

                          x, y, p = tt.locateImg(fanhui)
                          x2, y2, p2 = tt.locateImg(queren)
                          if p > 0.85 and p2 < 0.85:
                              x = random.randint(x - 5, x + 5)
                              y = random.randint(y - 5, y + 5)
                              mouse_click(x, y)

                          x, y, p = tt.locateImg(queren)
                          if p > 0.85:
                              x = random.randint(x - 15, x + 15)
                              y = random.randint(y - 5, y + 5)
                              mouse_click(x, y)
                              # time.sleep(1.5)


                  else:
                      print('没到9就失败那么多次')
                      # 这段是测试，可以不用的
                      x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
                      x2, y2, p2 = tt.locateImg(jingong)
                      if p > 0.95 and p2 < 0.85:
                          print('已经失败了')
                          x, y, p = tt.locateImg(shuaxin)
                          if p > 0.9:
                              x = random.randint(x - 15, x + 15)
                              y = random.randint(y - 5, y + 5)
                              mouse_click(x, y)

                      x, y, p = tt.locateImg(tupotu, region=(807, 412, 1140, 543))
                      x2, y2, p2 = tt.locateImg(jingong)
                      if p > 0.85 and p2 < 0.85:
                          x = random.randint(x - 180, x)
                          y = random.randint(y + 10, y + 80)
                          mouse_click(x, y)
                          print('识别突破9标志，打了一次')
                          turefaile = 1  # 打过一次9了
                          tupo_state = 9
                      pass

              elif tupo_state == 9:

                  x, y, p = tt.locateImg(tupotu, region=(139, 139, 473, 273))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.85 and p2 < 0.85:
                      tupo_state = 0
                      failed = 0
                      turefaile = 0
                      print('最后一次已经打过')

                  x, y, p2 = tt.locateImg(queding)
                  if p2 > 0.85:
                      x = random.randint(x - 15, x + 15)
                      y = random.randint(y - 5, y + 5)
                      mouse_click(x, y)
                      print('点击确定')
                      turefaile = 0
                      tupo_state = 0
                      failed = 0
                      shuaxinone = 0

                  x, y, p = tt.locateImg(dabuguo, region=(807, 412, 1140, 543))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.95 and turefaile == 1 and p2 < 0.85:
                      print('真失败了')
                      current_time = time.time()
                      print(current_time - last_refresh_time)
                      if shuaxinone == 1:
                          x, y, p = tt.locateImg(shuaxin)
                          if p > 0.9:
                              # time.sleep(240)
                              x = random.randint(x - 15, x + 15)
                              y = random.randint(y - 5, y + 5)
                              mouse_click(x, y)

                      if current_time - last_refresh_time >= 300:
                          x, y, p = tt.locateImg(shuaxin)
                          if p > 0.9:
                              # time.sleep(240)
                              x = random.randint(x - 15, x + 15)
                              y = random.randint(y - 5, y + 5)
                              mouse_click(x, y)

                  x, y, p = tt.locateImg(po, region=(807, 412, 1140, 543))
                  x2, y2, p2 = tt.locateImg(jingong)
                  if p > 0.80 and p2 < 0.85:
                      print('突破9成功')
                      current_time = time.time()
                      print(current_time - last_refresh_time)
                      if shuaxinone == 1:
                          x, y, p = tt.locateImg(shuaxin)
                          if p > 0.9:
                              x = random.randint(x - 15, x + 15)
                              y = random.randint(y - 5, y + 5)
                              mouse_click(x, y)

                      if current_time - last_refresh_time >= 300:
                          x, y, p = tt.locateImg(shuaxin)
                          if p > 0.9:
                              x = random.randint(x - 15, x + 15)
                              y = random.randint(y - 5, y + 5)
                              mouse_click(x, y)
                          else:
                              print('找不到刷新')


