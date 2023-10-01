#!/usr/bin/python
from configparser import ConfigParser

filename='/home/m_rezvukhin/data_science/credit_scoring/src/config/home_credit_db_cred.ini'
section='postgresql'

# create a parser
parser = ConfigParser()
# read config file
parser.read(filename)

# get section, default to postgresql
db_args = {}

if parser.has_section(section):
    params = parser.items(section)
    for param in params:
        db_args[param[0]] = param[1]
else:
    raise Exception('Section {0} not found in the {1} file'.format(section, filename))
