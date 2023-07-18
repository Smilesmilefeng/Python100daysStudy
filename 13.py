from random import randint
from time import time, sleep

from multiprocessing import Process
from os import getpid
from threading import Thread


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(3, 7)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (filename, time_to_download))


def main1():
    start = time()
    p1 = Process(target=download_task, args=('电影', ))
    p2 = Process(target=download_task, args=('资料', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


def main2():
    start = time()
    p1 = Thread(target=download_task, args=('电影', ))
    p2 = Thread(target=download_task, args=('资料', ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


if __name__ == '__main__':
    main2()
