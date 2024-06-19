import os
import time

import numpy
import win32api
import win32con
import win32gui
import cv2
import win32ui


#自己加
import logging
import time
import ctypes
from ctypes import wintypes


class LiuXingIT(object):


    #自己加的
    # 定义一些需要的常量
    WM_LBUTTONDOWN = 0x0201
    WM_LBUTTONUP = 0x0202
    MK_LBUTTON = 0x0001
    WM_RBUTTONDOWN = 0x0204
    WM_RBUTTONUP = 0x0205
    MK_RBUTTON = 0x0002
    WM_MBUTTONDOWN = 0x0207
    WM_MBUTTONUP = 0x0208
    MK_MBUTTON = 0x0010
    user32 = ctypes.WinDLL('user32', use_last_error=True)





    def __init__(self, h):
        self.h = h

    #自己家的
    def MAKELONG(self, low, high):
        return (high << 16) | (low & 0xFFFF)

    def mouseDoubleClick(self,x,y):
        x = int(x)
        y = int(y)
        position = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.h, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, position)
        win32api.PostMessage(self.h, win32con.WM_LBUTTONUP, None, position)

    def mouseClick(self, x,y,botton='left'):
        x = int(x)
        y = int(y)
        print(x,y)
        # position = win32api.MAKELONG(x, y)
        # if botton == 'left':
        #     win32api.PostMessage(self.h, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position)
        #     win32api.PostMessage(self.h, win32con.WM_LBUTTONUP, None, position)

        position = self.MAKELONG(x, y)
        # print(f"Attempting to click at {x}, {y} with button {botton}")

        if botton == 'left':
            success_down = self.user32.PostMessageW(self.h, self.WM_LBUTTONDOWN, self.MK_LBUTTON, position)
            # print(f"WM_LBUTTONDOWN success: {bool(success_down)}, at position {position}")
            if success_down:
                time.sleep(0.05)
                success_up = self.user32.PostMessageW(self.h, self.WM_LBUTTONUP, 0, position)
                # print(f"WM_LBUTTONUP success: {bool(success_up)}, at position {position}")
            elif botton == 'right':
                success_down = self.user32.PostMessageW(self.h, self.WM_RBUTTONDOWN, self.MK_RBUTTON, position)
                # print(f"WM_RBUTTONDOWN success: {bool(success_down)}, at position {position}")
                if success_down:
                    time.sleep(0.05)
                    success_up = self.user32.PostMessageW(self.h, self.WM_RBUTTONUP, 0, position)
                    # print(f"WM_RBUTTONUP success: {bool(success_up)}, at position {position}")
            elif botton == 'middle':
                success_down = self.user32.PostMessageW(self.h, self.WM_MBUTTONDOWN, self.MK_MBUTTON, position)
                # print(f"WM_MBUTTONDOWN success: {bool(success_down)}, at position {position}")
                if success_down:
                    time.sleep(0.05)
                    success_up = self.user32.PostMessageW(self.h, self.WM_MBUTTONUP, 0, position)
                    # print(f"WM_MBUTTONUP success: {bool(success_up)}, at position {position}")



        # elif botton == 'right':
        #     win32api.PostMessage(self.h, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, position)
        #     win32api.PostMessage(self.h, win32con.WM_RBUTTONUP, None, position)
        # elif botton == 'middle':
        #     win32api.PostMessage(self.h, win32con.WM_MBUTTONDOWN, win32con.MK_MBUTTON, position)
        #     win32api.PostMessage(self.h, win32con.WM_MBUTTONUP, None, position)

    def mouseDown(self,  x, y,botton='left'):
        x = int(x)
        y = int(y)
        position = win32api.MAKELONG(x, y)
        if botton == 'left':
            win32api.PostMessage(self.h, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position)
        elif botton == 'right':
            win32api.PostMessage(self.h, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, position)

    def mouseUp(self,  x, y,botton='left'):
        x = int(x)
        y = int(y)
        position = win32api.MAKELONG(x, y)
        if botton == 'left':
            win32api.PostMessage(self.h, win32con.WM_LBUTTONUP, None, position)
        elif botton == 'right':
            win32api.PostMessage(self.h, win32con.WM_RBUTTONUP, None, position)

    def mouseWheel(self, num, x, y):
        #负数往下，正数往上
        x = int(x)
        y = int(y)
        position = win32api.MAKELONG(x, y)
        param = (num * 120) << 16
        win32api.PostMessage(self.h, win32con.WM_MOUSEWHEEL, param, position)

    def mouseMove(self, x, y):
        x = int(x)
        y = int(y)
        position = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.h, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, position)

    def keyPress(self, num):
        num1 = win32api.MapVirtualKey(num, 0)
        dparam = 1 | (num1 << 16)
        uparam = 1 | (num1 << 16) | (1 << 30) | (1 << 31)
        win32api.PostMessage(self.h, win32con.WM_KEYDOWN, num, dparam)
        win32api.PostMessage(self.h, win32con.WM_KEYUP, num, uparam)

    def keyDown(self, num):
        num1 = win32api.MapVirtualKey(num, 0)
        dparam = 1 | (num1 << 16)
        win32api.PostMessage(self.h, win32con.WM_KEYDOWN, num, dparam)

    def keyUp(self, num):
        num1 = win32api.MapVirtualKey(num, 0)
        uparam = 1 | (num1 << 16) | (1 << 30) | (1 << 31)
        win32api.PostMessage(self.h, win32con.WM_KEYUP, num, uparam)

    #截屏
    def shot(self, region=None):
            result = win32gui.GetWindowRect(self.h)
            w = result[2] - result[0]
            h = result[3] - result[1]
            hdc = win32gui.GetWindowDC(self.h)
            dc = win32ui.CreateDCFromHandle(hdc)
            mdc = dc.CreateCompatibleDC()
            bm = win32ui.CreateBitmap()
            if region == None:
                bm.CreateCompatibleBitmap(dc, w, h)
                mdc.SelectObject(bm)
                mdc.BitBlt((0, 0), (w, h), dc, (0, 0), win32con.SRCCOPY)
            else:
                bm.CreateCompatibleBitmap(dc, region[2] - region[0], region[3] - region[1])
                mdc.SelectObject(bm)
                mdc.BitBlt((0, 0), (w, h), dc, (region[0], region[1]), win32con.SRCCOPY)

            # 检查是否成功创建了位图
            if bm.GetHandle() == 0:
                print("Error: Failed to create bitmap")
                return

            filename = '1.bmp'
            while os.path.exists(filename):
                try:
                    os.unlink(filename)
                except PermissionError:  # 文件被其他程序占用，等待一段时间再尝试删除
                    time.sleep(0.1)
                    continue
                break
            bm.SaveBitmapFile(mdc, filename)  # 保存新文件
            win32gui.DeleteObject(bm.GetHandle())
            mdc.DeleteDC()
            dc.DeleteDC()
            win32gui.ReleaseDC(self.h, hdc)

    def hudushot(self, region=None):
            result = win32gui.GetWindowRect(self.h)
            w = result[2] - result[0]
            h = result[3] - result[1]
            hdc = win32gui.GetWindowDC(self.h)
            dc = win32ui.CreateDCFromHandle(hdc)
            mdc = dc.CreateCompatibleDC()
            bm = win32ui.CreateBitmap()
            if region == None:
                bm.CreateCompatibleBitmap(dc, w, h)
                mdc.SelectObject(bm)
                mdc.BitBlt((0, 0), (w, h), dc, (0, 0), win32con.SRCCOPY)
            else:
                bm.CreateCompatibleBitmap(dc, region[2] - region[0], region[3] - region[1])
                mdc.SelectObject(bm)
                mdc.BitBlt((0, 0), (w, h), dc, (region[0], region[1]), win32con.SRCCOPY)

           # ---------------------------中间是自己修改的
            filename = '2.bmp'
            while os.path.exists(filename):
                try:
                    os.unlink(filename)
                except PermissionError:  # 文件被其他程序占用，等待一段时间再尝试删除
                    time.sleep(0.1)
                    continue
                break
            bm.SaveBitmapFile(mdc, filename)  # 保存新文件
            # ---------------------------自己修改的


            #bm.SaveBitmapFile(mdc, '2.bmp')#截图为2.bmp
            win32gui.DeleteObject(bm.GetHandle())
            mdc.DeleteDC()
            dc.DeleteDC()
            win32gui.ReleaseDC(self.h, hdc)


    def locateImg(self, src, region=None):
        self.shot(region)#截图
        img=cv2.imread('1.bmp')#读取图片
        template = cv2.imread(src)#传入参数图片转模式
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if region != None:
            return int(max_loc[0] + region[0]), int(max_loc[1] + region[1]), max_val
        else:
            return int(max_loc[0]), int(max_loc[1]), max_val

    def locateAllImg(self, src, region=None):
        res = []
        self.shot(region) #截图
        img=cv2.imread('1.bmp')  #读取截图


        template = cv2.imread(src)
        # result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        result = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
        yloc, xloc = numpy.where(result <= 0.002)#原本是0.98
        for x, y in zip(xloc, yloc):
            if region != None:
                res.append((x + region[0], y + region[1]))
            else:
                res.append((x, y))
        return res


    #灰度图
    def locateAllHuDuImg(self, src, region=None):
        res = []
        self.hudushot(region)
        img = cv2.imread('2.bmp', cv2.IMREAD_GRAYSCALE)
        # cv2.imshow('Gray image', img)
        # cv2.waitKey(0) #等待，必要的步骤，不然一闪而过
        # cv2.destroyAllWindows()#关闭所以的窗口

        template = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        # cv2.imshow('Gray image1', template)
        # cv2.waitKey(0) #等待，必要的步骤，不然一闪而过
        # cv2.destroyAllWindows()#关闭所以的窗口

        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.80
        yloc, xloc = numpy.where(result >= threshold)

        # 计算每个匹配点的匹配度并加入到结果列表中
        for x, y in zip(xloc, yloc):
            match_prob = result[y, x]  # 获取对应位置的匹配度
            if region != None:
                res.append(((x + region[0], y + region[1]), match_prob))
            else:
                res.append(((x, y), match_prob))
        return res


    def getPixel(self, x, y):
        self.shot()
        img=cv2.imread('1.bmp')
        return img[y, x][::-1]


