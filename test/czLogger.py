import os
import logging
import time

class czLogger(object):
    '''
    @summary:日志处理对象,对logging的封装
    '''

    def __init__(self, name='Logger',log_type = 'tool', log_file = 'tool'):

        self.logger = logging.getLogger(name)
        self.init_logger(log_type,log_file)
        # self.init_logger('tool','tool')
        # self.init_logger('AT','ATlog')

    def init_logger(self, log_type, log_file):
        if log_type == 'tool':
            # self.logger.setLevel(logging.CRITICAL)
            # self.logger.setLevel(logging.ERROR)
            # self.logger.setLevel(logging.WARNING)
            # self.logger.setLevel(logging.INFO)
            self.logger.setLevel(logging.DEBUG)

            # 日志样式
            fm_stream = logging.Formatter(
               "[%(asctime)s] [%(levelname)s] %(filename)s %(funcName)s %(lineno)s : %(message)s")
            fh = logging.FileHandler('./LOG/'+log_file+time.strftime('-%Y.%m.%d %H:%M:%S',time.localtime(time.time()))+'.log', mode='a')
            # 屏幕输出日志
            fh.setFormatter(fm_stream)
            stream = logging.StreamHandler()
            # stream.setLevel(logging.DEBUG)
            stream.setFormatter(fm_stream)

            self.logger.addHandler(fh)
            self.logger.addHandler(stream)
        elif log_type == 'AT':
            self.logger.setLevel(logging.INFO)
            formatter = logging.Formatter('[%(asctime)s] %(message)s')

            fh = logging.FileHandler('./LOG/'+log_file+time.strftime('-%Y.%m.%d %H:%M:%S',time.localtime(time.time()))+'.log', mode='a')
            fh.setFormatter(formatter)
            sh = logging.StreamHandler()
            sh.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.logger.addHandler(sh)
        # elif log_type == 'ERROR':
        #     self.logger.setLevel(logging.ERROR)
        #     formatter = logging.Formatter(
        #         "[%(asctime)s] %(filename)s %(funcName)s %(lineno)s %(levelname)s - %(message)s",
        #         "%m-%d %H:%M:%S")
        #
        #     fh = logging.FileHandler('./LOG/'+log_file+time.strftime('-%Y.%m.%d %H:%M:%S',time.localtime(time.time()))+'.log', mode='a')
        #     fh.setFormatter(formatter)
        #     sh = logging.StreamHandler()
        #     sh.setFormatter(formatter)
        #     self.logger.addHandler(fh)
        #     self.logger.addHandler(sh)



    def update_kwargs(self, kwargs, colorcode):
        try:
            fn, lno, func = self.logger.findCaller()
            fn = os.path.basename(fn)
        except Exception as ddd:
            fn, lno, func = "(unknown file)", 0, "(unknown function)"

        if not "extra" in kwargs:
            kwargs["extra"] = {}

        kwargs["extra"]["myfn"] = fn
        kwargs["extra"]["mylno"] = lno
        kwargs["extra"]["myfunc"] = func
        kwargs["extra"]["colorcode"] = colorcode
        kwargs["extra"]["mymodule"] = ""

    def debug(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "0")  # 原色
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "32")  # 绿色
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "33")  # 黄色
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "31")  # 红色
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "31")  # 红色
        self.logger.critical(msg, *args, **kwargs)

    def getlog(self):
        return self.logger

log = czLogger("atlog")

if __name__ == '__main__':
    atlog = czLogger("ATLOG", "AT", "atlog")
    toollog = czLogger("toollog", "tool", "tool")
    # errorlog = czLogger("errorlog","ERROR","error")
    atlog.info("FUN_FTP_123 START")
    atlog.info("request %s","AT")
    atlog.info("response %s","OK")
    atlog.info("FUN_FTP_123 END")

    toollog.debug("---debug")
    toollog.error("---error")
    toollog.warning("---warning")
    toollog.info("---info")
    toollog.critical("---critical")