# coding=utf-8

import os, time, random
from multiprocessing import Process, Pool


def run_proc(name):
    print("Process child process %s (%s)..." % (name, os.getpid()))


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, end - start))


if __name__ == '__main__':
    print("Parent process %s " % os.getpid())
    # Pool()线程池数量，默认是cpu核心数
    p1 = Pool(5)
    for i in range(5):
        p1.apply_async(long_time_task, args=(i,))
    print("waiting for all subprocesses done...")
    p1.close()
    p1.join()
    print("all subprocesses done.")
