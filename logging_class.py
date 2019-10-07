import logging

class Logger(object):
    #logging.basicConfig(filename='cmdsql.log', level=logging.INFO, format='[%(asctime)s] - [%(levelname)s] - %(message)s')
    def __init__(self, name='namelog',level=logging.DEBUG):
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        file_handler = logging.FileHandler('%s.log' % name, 'w')
        formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)        
        
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
        
def Main():
    log = Logger()    
    log.debug('debug log')
    log.info('info log')
    log.warning('warning log')
    log.error('error log')

    
def Main():    