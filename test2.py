import PythonLogger as logger


class test2:
    '''This is the class to test the PythonLogger'''
    def __init__(self, name, id):
        self.name = name
        self.id = id


    def logSomething(self):
        my_log = logger.getLogger()
        my_log.info(f'This is {self.name} and my id is {self.id}')
        my_log.debug("This is debug in test2.")
        my_log.info("This is the info in test2.")
        my_log.warning("This is the warning in test2.")
        my_log.error("This is the error in test2.")
        my_log.critical("This is the critical in test2.")
        my_log.info(f'I finished my log')
