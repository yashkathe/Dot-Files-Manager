import json
import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dot_files_manager import check_json_config
# from src.dot_files_manager import *


check_json_config()

# file = 'd_manager.json'
#
# with open(file, 'r') as rf:
#     
#     f = json.load(rf)
#
#     for line in f['dot_files']:
#         print(line)
#


