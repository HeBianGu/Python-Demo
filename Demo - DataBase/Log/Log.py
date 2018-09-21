# coding=utf-8
import logging
import os
import datetime

"""
 日志操作类
"""
class LoggerService(object):
    def __init__(self, folderPath):
        """
        初始化日志路径
        """
        self.log_path = str(folderPath)
        self.time = datetime.datetime.now().strftime('%Y-%m-%d')
        self.hour = datetime.datetime.now().strftime('%H')
        self.log = logging.getLogger(self.time + '_' + self.hour)
        self.log.setLevel(logging.INFO)

    def info(self, msg):
        """
         写运行日志
        """
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        hour = datetime.datetime.now().strftime('%H')
        if time != self.time or hour != self.hour or len(self.log.handlers) == 0:
            self.init()
        self.log.info(msg)
        print(msg)

    def error(self, msg):
        """
         写错误日志
        """
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        hour = datetime.datetime.now().strftime('%H')
        if time != self.time or hour != self.hour or len(self.log.handlers) == 0:
            self.init()
        self.log.error(msg)
        print(msg)

    def init(self):
        """
         初始化日志格式
        """
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        hour = datetime.datetime.now().strftime('%H')
        log_path_info = self.log_path + "\\" + time
        self.log = logging.getLogger(time + '_' + hour)
        self.log.setLevel(logging.INFO)
        if not os.path.exists(log_path_info):
            os.makedirs(log_path_info)
        log_path_info = log_path_info + "\\" + time + "_" + hour + '.log'
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        if len(self.log.handlers) == 0:
            info_h = logging.FileHandler(log_path_info)
            info_h.setFormatter(formatter)
            self.log.addHandler(info_h)


if __name__ == '__main__':
    t_log = LoggerService("F:\python\log")
    t_log.error('error-5')
    t_log.info('info-5')
    t_log.info('info-6')
    # t_log.release()

    print("End")
