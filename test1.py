import PythonLogger as mylog
from test2 import test2




def main():
    print("Test1")
    mytest2 = test2("myFirstClass", 1)


    mylog.setup()
    logger = mylog.getLogger()
    logger.warning("Hello World!")
    mytest2.logSomething()


if __name__ == "__main__":
    main()