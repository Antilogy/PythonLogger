# PythonLogger
A project that keeps track of my skeleton code for implementing loggers in python apps.


#How to use
```
import PythonLogger as mylog

mylog.setup()
logger = mylog.getLogger()
logger.warning("Hello World!")
```


#If running the file in production
This code will automatically log to a file in "{base directory of main.py}/tmp/{main}.log"
For example, if the main file of your project is project.py and this file is on your desktop it will save the logs in the following directory:
```
C:\Users\Bob\Desktop\tmp\project.log
```

Otherwise it will print to the cmd prompt.

