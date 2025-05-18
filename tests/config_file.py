import json
import os

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
