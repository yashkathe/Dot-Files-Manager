import json
import os

conf_file = "d_manager.json"
user_home = os.path.expanduser("~")


def create_json_config(conf_file=conf_file):

    emit_folder_name = "dot_files_manager"

    os.makedirs(os.path.join(user_home, emit_folder_name), exist_ok=True)

    # skeleton for config file
    data = {
        "dot_files": {"directories": [], "files": []},
        "emit_folder": os.path.join(user_home, emit_folder_name),
        "git-repository": "",
    }

    # create config file
    if os.path.exists(conf_file):
        print("config file already exists")
        return 1

    else:
        with open(conf_file, "w") as wf:
            json.dump(data, wf, indent=4)

        print("created empty config file")
        return 0


def check_json_config(conf_file=conf_file):

    with open(conf_file, "r") as rf:

        conf_file = json.load(rf)

        # error & exit - if emit_directory is empty
        for emit_f in conf_file["emit_folder"]:
            if not emit_f:
                print("emit_directory is empty")
                print(
                    "check the config file and add emit directory with full path where dot files should be copied"
                )
                return 1

        # warn - if no files are found print a warning
        for entry in conf_file["dot_files"]:
            if not conf_file["dot_files"][entry]:
                print(f"No entries found for dot file {entry}")
                print(f"No entries found for dot {entry}")

        return 0
