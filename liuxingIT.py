import numpy
import win32api
import win32con
import win32gui
import cv2
import win32ui


class LiuXingIT(object):

    def __init__(self, h):
        self.h = h



    def mouseDoubleClick(self,x,y):
        x = int(x)
        y = int(y)
        position = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.h, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, position)
        win32api.PostMessage(self.h, win32con.WM_LBUTTONUP, None, position)

    def mouseClick(self, x,y,botton='left'):
        x = int(x)
        y = int(y)
        position = win32api.MAKELONG(x, y)
        if botton == 'left':
            win32api.PostMessage(self.h, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position)
            win32api.PostMessage(self.h, win32con.WM_LBUTTONUP, None, position)
        elif botton == 'right':
            win32api.PostMessage(self.h, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, position)
            win32api.PostMessage(self.h, win32con.WM_RBUTTONUP, None, position)
        elif botton == 'middle':
            win32api.PostMessage(self.h, win32con.WM_MBUTTONDOWN, win32con.MK_MBUTTON, position)
            win32api.PostMessage(self.h, win32con.WM_MBUTTONUP, None, position)

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
            bm.SaveBitmapFile(mdc, '1.bmp')#截图为1.bmp
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
            bm.SaveBitmapFile(mdc, '2.bmp')#截图为2.bmp
            win32gui.DeleteObject(bm.GetHandle())
            mdc.DeleteDC()
            dc.DeleteDC()
            win32gui.ReleaseDC(self.h, hdc)


    def locateImg(self, src, region=None):
        self.shot(region)#截图区域
        img=cv2.imread('1.bmp')#读取图片
        template = cv2.imread(src)#将要对比的图转模式
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if region != None:
            return int(max_loc[0] + region[0]), int(max_loc[1] + region[1]), max_val
        else:
            return int(max_loc[0]), int(max_loc[1]), max_val

    def locateAllImg(self, src, region=None):
        res = []
        self.hudushot(region) #截图
        img=cv2.imread('2.bmp')  #读取截图
        template = cv2.imread(src)
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = numpy.where(result >= 0.98)
        for x, y in zip(xloc, yloc):
            if region != None:
                res.append((x + region[0], y + region[1]))
            else:
                res.append((x, y))
        return res


    #灰度图
    def locateAllHuDuImg(self, src, region=None):
        res = []
        self.shot(region)
        img = cv2.imread('1.bmp', cv2.IMREAD_GRAYSCALE)
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


