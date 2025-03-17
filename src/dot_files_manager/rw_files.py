import json
import os
import subprocess

# Function to sync all Dot Files (not Directories) 
def check_file_diff(conf_file):

    # check files only
    with open(conf_file, "r") as rf:

        # function variables
        load_conf = json.load(rf)
        emit_dir = load_conf["emit_folder"]

        if not emit_dir:
            return 1

        # check if dot files exist
        if not load_conf["dot_files"]["files"]:
            print(f"no dot files regiesterd in {conf_file}")
            return 1

        # start sync
        print(f"starting to sync dot-files from {conf_file}\n")
        for df in load_conf["dot_files"]["files"]:

            if os.path.exists(df):

                emit_path = f"{emit_dir}/{ os.path.basename(df)}"

                # copy file from original directory to emit directory
                cpy = subprocess.run(
                    f"cp {df} {emit_path}", shell=True, capture_output=True, text=True
                )

                if cpy.returncode != 0:
                    print(cpy.stderr)

            else:
                print(f"{df} not found")

    print("successfully synced all the files")
