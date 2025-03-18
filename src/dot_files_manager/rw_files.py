import json
import os
import subprocess
from collections import defaultdict

from hash_files import are_similar_files


# Copy Files
def copy_files(src, dist):
    cp_process = subprocess.run(
        f"cp {src} {dist}",
        shell=True,
        capture_output=True,
        text=True,
    )

    return cp_process.stderr if cp_process.returncode != 0 else 0


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
        print(f"\nStarting to Sync dot-files from {conf_file}\n")
        freq = defaultdict(int)

        for df in load_conf["dot_files"]["files"]:

            # if file mentioned in conf exists
            if os.path.exists(df):

                emit_path = f"{emit_dir}/{ os.path.basename(df)}"

                if not os.path.exists(emit_path):

                    print(f"changes detected -> {os.path.basename(df)}")
                    copy_files(df, emit_path)
                    freq["change"] += 1

                elif not are_similar_files(df, emit_path):

                    print(f"new file detected -> {os.path.basename(df)}")
                    copy_files(df, emit_path)
                    freq["new"] += 1

                else:

                    freq["same"] += 1

            else:
                print(f"{df} not found")

    print("\n=========================================")
    print(f"✅ Total Files Scanned: {sum(freq.values())}")
    print(f"└─✨ New Files: {freq['new']}")
    print(f"└─✨ Re-uploaded Files: {freq['change']}")
    print(f"└─✨ Un-touched Files: {freq['same']}")
    print("=========================================\n")


# Function to Sync all Files within Directories
