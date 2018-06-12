import argparse
import logging
import os

from ConfigParser import SafeConfigParser

#datetime formats
DTFMT = '%Y%m%d%H%M%S' # YYYYmmddHHMMSS datetime parse format

description = """
This is the default description.
"""
arg_parser = argparse.ArgumentParser( description=description, 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter )

arg_parser.add_argument('--log', action='store'     
    , default='INFO' , type=str
    , help="Log level"
    , choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    )

arg_parser.add_argument('--log_name', action='store'     
    , default='LOG' , type=str
    , help="Change log name"
    )

arg_parser.add_argument('--config_filename', action='store'     
    , default='config.ini' , type=str
    , help="Path of configuration file"
    )

args   = None
log    = None
config = None

def init():
  global args
  global log
  global config

  args = arg_parser.parse_args()

  logging.basicConfig( level   = getattr(logging, args.log, 'CRITICAL')
                    , format  = '%(asctime)s %(levelname)-8s %(message)s'
                    , datefmt = '%Y-%m-%d %H:%M:%S'
                    )

  log    = logging.getLogger(name=args.name)

  config = SafeConfigParser()
  config.read(args.config_filename)
  modified_time = os.stat(args.config_filename).st_mtime

def reload_config():
  new_modified_time = os.stat(self.config_filename).st_mtime
  if new_modified_time != modified_time:
    log.info("Reloading configuration file {}".format(self.config_filename))
    config.read(args.config_filename)
    self.modified_time = new_modified_time

