import argparse
import configparser
import logging
import os


#datetime formats
DTFMT = '%Y-%m-%dT%H:%M:%S' # YYYY-mm-ddTHH:MM:SS datetime parse format

description = """
Execute PPM generation

(Command line arguments override configuration file settings)
"""
arg_parser = argparse.ArgumentParser( description=description, 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter )

arg_parser.add_argument('--config_filename', action='store'     
    , default='config.ini' , type=str
    , help="Path of configuration file"
    )

arg_parser.add_argument('--logging.level', action='store'
    , type=str
    , help="Log level"
    , choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    )

arg_parser.add_argument('--logging.name', action='store'     
    , type=str
    , help="Change log name"
    )

args          = None
log           = None
config        = None
modified_time = 0

def init():
    global args
    global log
    global config
    global modified_time

    args = arg_parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_filename)
    modified_time = os.stat(args.config_filename).st_mtime

    log_level = getattr(args, 'logging.level') or config.get('logging', 'level'   , fallback='CRITICAL')
    log_name  = getattr(args, 'logging.name' ) or config.get('logging', 'log_name', fallback='LOG'     )

    logging.basicConfig( level   = log_level
                       , format  = '%(asctime)s RSTORM-PPM:%(process)d %(levelname)-8s %(message)s'
                       , datefmt = DTFMT
                       )
    log = logging.getLogger(name=log_name)


def reload_config():
    global modified_time
    new_modified_time = os.stat(args.config_filename).st_mtime
    if new_modified_time != modified_time:
        log.info("Reloading configuration file {}".format(args.config_filename))
        config.read(args.config_filename)
        modified_time = new_modified_time


if __name__=="__main__":
    init()
    reload_config()
    log.info("PROGRAM START")
    log.info("PROGRAM END")

  
