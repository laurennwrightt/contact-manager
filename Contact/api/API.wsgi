#!/usr/bin/python3.8

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/flaskapi/')
from API import api as application
application.secret_key = '12345'