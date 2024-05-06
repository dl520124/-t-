
import win32gui
import time
import cv2
from liuxingIT import LiuXingIT
import random


if __name__ == '__main__':
    roufeng = './liudao/roufeng.png'
    zhan = './liudao/zhan.png'
    putong = './liudao/putong.png'
    tiaozhan = './liudao/tiaozhan.png'
    yaoshu = './liudao/yaoshu.png'
    xuanzejineng = './liudao/xuanzejineng.png'
    hundun = './liudao/hundun.png'
    baoxiang = './liudao/baoxiang.png'
    kaiqi = './liudao/kaiqi.png'
    kaiqi2 = './liudao/kaiqi2.png'



    handle = win32gui.FindWindow('Qt5156QWindowIcon', 'MuMu模拟器12')
    print(handle)
    h = win32gui.FindWindowEx(handle, None, 'Qt5156QWindowIcon', 'MuMuPlayer')
    print(h)
    tt = LiuXingIT(h)
    while True:
        print('循环回来')
        u = 0
        j = 0
        x, y, p = tt.locateImg(roufeng, None)
        if  p>0.85:
            # x = random.randint(288,368)
            y = random.randint(584, 609)
            tt.mouseClick(x,y)
            print('点击开始选择柔风')
        else:
            pass

        x, y, p = tt.locateImg(zhan)
        if p > 0.85:
            print('找到战斗')
            x, y, p = tt.locateImg(zhan, region=(145, 247, 421, 465))  #145  247
            if p > 0.85:
                x = random.randint(x-1, x+1)
                y = random.randint(y-3, y+3)
                tt.mouseClick(x, y)
                print('点击左边的战斗')
            else:
                pass
            x, y, p = tt.locateImg(zhan)
            x = random.randint(x - 1, x + 1)
            y = random.randint(y - 1, y + 1)
            tt.mouseClick(x, y)
            print('点击战斗')
        else:
            pass

        x, y, p = tt.locateImg(putong, region=(675, 207, 785, 425))  # 145  247
        if p > 0.85:
            x = random.randint(x - 1, x + 1)
            y = random.randint(y - 1, y + 5)
            tt.mouseClick(x, y)
            print('点击右边的普通')
        else:
            print('没有识别到普通')
            pass
        x, y, p = tt.locateImg(tiaozhan)  # 145  247
        if p > 0.85:
            x = random.randint(1142, 1219)
            y = random.randint(597, 657)
            tt.mouseClick(x, y)
            print('点击挑战')
            time.sleep(1)

            while True:
                num = 0
                x, y, p = tt.locateImg(yaoshu, region=(779, 627, 1273, 708))  # 145  247
                if p > 0.85:
                    print('已经是妖术')
                    num +=1
                    pass
                else:
                    x = random.randint(x - 1, x + 1)
                    y = random.randint(y, y + 3)
                    tt.mouseClick(x, y)
                    print('选择普攻')
                if num>5:
                    break
        else:
            pass

        x, y, p = tt.locateImg(xuanzejineng)  # 145  247
        if p > 0.85:
            print('选择技能画面')
            x, y, p = tt.locateImg(roufeng)  # 145  247
            if p > 0.85:
                y = random.randint(584, 609)
                tt.mouseClick(x, y)
                print('点击柔风')
            else:
                x = random.randint(1046, 1139)
                y = random.randint(587, 613)
                tt.mouseClick(x, y)
                print('没有柔风选恢复')
                pass
        else:
            pass


        x, y, p = tt.locateImg(hundun)  # 145  247
        if p > 0.85:
            x = random.randint(x - 1, x + 1)
            y = random.randint(y - 1, y + 2)
            tt.mouseClick(x, y)
            print('点击混沌')
        else:
            pass

        x, y, p = tt.locateImg(baoxiang)  # 145  247
        if p > 0.85:
            x = random.randint(x - 1, x + 1)
            y = random.randint(y - 1, y + 2)
            tt.mouseClick(x, y)
            print('点击混沌')
        else:
            pass

        x, y, p = tt.locateImg(kaiqi2)  # 145  247
        if p > 0.85:
            x = random.randint(x - 1, x + 1)
            y = random.randint(y - 1, y + 2)
            tt.mouseClick(x, y)
            print('点击开启')
        else:
            print('没有找到开启')
            pass




