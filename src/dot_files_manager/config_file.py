import json
import os
import shutil
import subprocess

from src.dot_files_manager.hash_files import are_similar_files, get_file_hash

user_home = os.path.expanduser("~")


# create emit directory and JSON config file
def create_json_config(conf_file):

    emit_folder_name = "dot_files_manager"

    # create directory for emit folder
    os.makedirs(os.path.join(user_home, emit_folder_name), exist_ok=True)

    # skeleton for config file
    data = {
        "dot_files": {"directories": [], "files": []},
        "emit_folder": os.path.join(user_home, emit_folder_name),
        "git-repository": "",
    }

    # create config file
    if os.path.exists(conf_file):
        print("Not Creating a New Config File as it Already Exists\n")
        return 1

    else:
        with open(conf_file, "w") as wf:
            json.dump(data, wf, indent=4)

        print(f"Created an Empty Config File at {os.getcwd()}/{conf_file}\n")
        return 0


def check_json_config(conf_file):

    with open(conf_file, "r") as rf:

        load_conf = json.load(rf)

        # error & exit - if emit_directory is empty
        for emit_f in load_conf["emit_folder"]:
            if not emit_f:
                print("Entry for emit_directory is empty")
                print(
                    "Check the Config File and add Emit Directory with Full Path where Dot Files should be copied"
                )
                return 1

        # warn - if no files are found print a warning
        for entry in load_conf["dot_files"]:
            if not load_conf["dot_files"][entry]:
                print(f"No Entries found for Dot {entry}")

    return 0


def edit_config_file(conf_file):

    # __file__ - path of current executing file
    config_path = os.path.join(os.path.dirname(__file__), f"../../{conf_file}")

    if not os.path.isfile(config_path):
        print(f"Config file '{conf_file}' not found!")
        print("Please run: make install")
        return 1

    prev_hash = get_file_hash(config_path)

    # load config file in text_editor

    text_editors = ["nano", "vim", "code"]

    for text_editor in text_editors:

        if shutil.which(text_editor):
            process = subprocess.run(
                [text_editor, config_path],
            )

            if process.returncode == 0:
                new_hash = get_file_hash(config_path)

                if prev_hash != new_hash:
                    print("Config File Updated")
                else:
                    print("No Changes to Config File")
                return 0
            else:
                print(f"failed to open config file with {text_editor}")
                return 1

    print(f"No Text Editors found: {','.join(text_editors)}")
    return 1
