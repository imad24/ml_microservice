# -*- coding: utf-8 -*-
"""This file contains the global settings of the package
Make sure you set the following environement variables:
        APPPATH: the absolute path to the application folder
"""
import os
import sys
import logging
import json
from dotenv import find_dotenv, load_dotenv
import datetime

load_dotenv(find_dotenv())

#Setting the app directory
global app_dir
global logging_level
app_dir = os.path.normpath(os.getenv("APPPATH"))
logging_level = logging.INFO



def init(working_directory=None):
    
    global globalConfigFile
    global userConfigFile
    global options

    # global path
    app_dir = os.path.normpath(os.getenv("APPPATH"))
    

    source_directory = os.path.normpath(os.getenv("SHAREDFOLDER"))

    globalConfigFile = os.path.join(app_dir,'config.json')
    userConfigFile = os.path.join(source_directory,'config.json')
    #set folders structure
    _set_folders(source_directory, working_directory = working_directory)

    # load global settings from config file
    cfg_file = globalConfigFile

    #set user config file
    if os.path.isfile(userConfigFile): 
            cfg_file = userConfigFile 
    
    with open(cfg_file) as cfg:
        options = json.load(cfg)

    if "log_level" in options:
        _set_logging_level(options["log_level"])

def get_logger(name):
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_fmt)

    logger = logging.getLogger(name)

    # clean any set logger
    if (logger.hasHandlers()):
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)
     
    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging_level)
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
 
    now = datetime.datetime.now()
    # create error file handler and set level to error
    log_file_name = "error_%s.log"%(now.strftime("%d_%m_%Y"))
    handler = logging.FileHandler(os.path.join(app_dir, log_file_name),"a", encoding=None, delay="true")
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
 
    # create debug file handler and set level to debug
    log_file_name = "app_%s.log"%(now.strftime("%d_%m_%Y"))
    handler = logging.FileHandler(os.path.join(app_dir, log_file_name),"a")
    handler.setLevel(logging_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
    





def set_user_config_file(filepath):
	global options
	userConfigFile = filepath
	if os.path.isfile(userConfigFile): 
		cfg_file = userConfigFile 
	with open(cfg_file) as cfg:
        options = json.load(cfg)
	if "log_level" in options:
        _set_logging_level(options["log_level"])
    
def _set_logging_level(verbose):
        global logging_level
        levels= {
        "DEBUG":logging.DEBUG,
        "INFO":logging.INFO,
        "WARNING":logging.WARNING,
        "ERROR":logging.ERROR,
        "CRITICAL":logging.CRITICAL,
        "FATAL":logging.FATAL
        }
        alias = { 0:"DEBUG", 1:"INFO",2:"WARNING", 3:"ERROR", 4:"CRITICAL", 5:"FATAL"}
        if verbose in levels: 
                logging_level = levels[verbose]
        elif verbose in range(len(levels)):
                logging_level = levels[alias[verbose]]

def get_option(key):
        #checking if the app is correctly set for this instance run
        test_setting()
        return options.get(key, None)

def set_options(options):
    with open(userConfigFile, 'w') as cfg:
        json.dump(options, cfg)
      
if __name__ == '__main__':
    init()