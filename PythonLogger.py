import os, logging.config, logging.handlers, sys
from pathlib import Path

#setup logging
logger = None
logging_config = {
        'version':1,
        'disable_existing_loggers':False,
        'formatters':{
            'detailed':{
                'class': 'logging.Formatter',
                'format':'%(asctime)s-%(levelname)s-[%(filename)s:%(lineno)s] %(message)s',
                'datefmt':'%m-%d-%Y:%H:%M:%S',
            }
        },
        'handlers':{
            'file':{
                'level':'WARNING',
                'class':'logging.FileHandler',
                'filename':'main.log',
                'mode':'a',
                'formatter':'detailed',
                

            },
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
                'formatter':'detailed'
                
            }
        },
        'loggers':{
            'dev':{
                'handlers':['console'],
                'propagate':True,
                'level':'DEBUG',
            },
            'prod':{
                'handlers':['file'],
                'propagate':True,
                'level':'WARNING',
            }
        },
    }
temp_file = logging_config['handlers']['file']['filename']
    #select loggers



def setup(*name):
    # use name of the main application
    log_name = ""
    if(name):
        log_name = name
    else:
        log_name = os.path.splitext(os.path.basename(__file__))[0]

    # Create the directory for the file
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, "tmp")
    file_path = os.path.join(full_path, f'{log_name}.log')
    Path(full_path).mkdir(parents = True, exist_ok = True)
    if(not sys.gettrace()):
        global logger
        #assume code doesn't run on debugger, its on production
        logging_config['handlers']['file']['filename'] = file_path
        logging.config.dictConfig(logging_config)
        logger = logging.getLogger('prod')

    else:
        logging.config.dictConfig(logging_config)
        logger = logging.getLogger('dev')

def getLogger():
    return logger

def main():
    # Input code to test here
    pass

if __name__ == "__main__":
    main()


