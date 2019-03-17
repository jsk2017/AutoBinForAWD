# -*- coding : utf-8 -*-
# file__name 192.168.43.252.py
import sys
import os
# add modul path
modul_path = os.path.abspath('.')
sys.path.append(modul_path)
# import handle function
from  autoUtil  import *
auto_get_submit('192.168.43.252',10000) 
    