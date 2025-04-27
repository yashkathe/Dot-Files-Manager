import argparse

from src.dot_files_manager.config_file import check_json_config, create_json_config, edit_config_file 
from src.dot_files_manager.rw_files import check_file_diff, check_folder_diff

# argparse setup

parser = argparse.ArgumentParser(description="A simple script to sync dotfiles and directories to a central emit_folder for backup or management.")

parser.add_argument("-e", "--edit", help="edit the config file (d_manager.json)", action="store_true")
parser.add_argument("-r", "--run", help="sync the dot files with your emit directory", action="store_true")

args = parser.parse_args()

# name of config file

json_config_filename = "d_manager.json"

if __name__ == "__main__":
    if args.edit:
        edit_config_file(json_config_filename)
    else:
        create_json_config(json_config_filename)
        check_json_config(json_config_filename)
        check_file_diff(json_config_filename)
        check_folder_diff(json_config_filename)                     
