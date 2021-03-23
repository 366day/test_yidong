#导包
import logging.handlers
import time
class GetLogger:
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            #获取日志器
            cls.logger = logging.getLogger()
            #获取日志器级别
            cls.logger.setLevel(logging.INFO)
            #获取文件处理器
            th = logging.handlers.TimedRotatingFileHandler(filename="../yidong_web/IP_Intelligent_system/log/{}.log".
                                                           format(time.strftime("%Y_%m_%d %H_%M_%S")),
                                                            when="midnight",
                                                            interval=1,
                                                            backupCount=30,
                                                            encoding="utf-8")
            #获取格式器
            fmt = '%(asctime)s - %(pathname)s [line:%(lineno)d] - %(levelname)s: %(message)s'
            fm = logging.Formatter(fmt)
            #把日志器添加到处理器
            th.setFormatter(fm)
            #把处理器添加到日志器
            cls.logger.addHandler(th)
        return cls.logger