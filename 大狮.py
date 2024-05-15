import os,time,shutil



if __name__ == '__main__':

  targetdir = r"F:\yys\阴阳师百鬼夜行\data"


files = []
while True:
    files = os.listdir(targetdir)
    for fileitem in files:
        fileroute = os.path.join(targetdir, fileitem)
        if os.path.isfile(fileroute):
            os.remove(fileroute)
        elif os.path.isdir(fileroute):
            shutil.rmtree(fileroute,True)
    print("%s 目录文件和文件夹删除成功" % (time.strftime("%Y/%m/%d %H:%M:%S")))
    time.sleep(60)
