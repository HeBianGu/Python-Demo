# coding=utf-8

import os, time, random
from multiprocessing import Process, Pool


def run_proc(name):
    print("Process child process %s (%s)..." % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s " % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    p = Process(target=run_proc, args=("test",))
    print("child process will start.")
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print("child process end.")
