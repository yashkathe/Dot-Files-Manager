import json
import os
import subprocess
from collections import defaultdict

from hash_files import are_similar_files


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
        freq = defaultdict(int)
        
        for df in load_conf["dot_files"]["files"]:

            if os.path.exists(df):

                emit_path = f"{emit_dir}/{ os.path.basename(df)}"


                if not os.path.exists(emit_path) or not are_similar_files(df, emit_path):

                    print(f"changes detected in {os.path.basename(df)}")

                    # copy file from original directory to emit directory
                    cpy = subprocess.run(
                        f"cp {df} {emit_path}",
                        shell=True,
                        capture_output=True,
                        text=True,
                    )

                    if cpy.returncode != 0:
                        print(cpy.stderr)
                        continue
                    
                    freq['change'] += 1

                else:

                    freq['same'] += 1

            else:
                print(f"{df} not found")

    print("\n=== Successfully Synced all the Files ===")
    print(f"Total Files Scanned: {sum(freq.values())}")
    print(f"Files re-uploaded: {freq['change']}")
    print(f"Files un-touched: {freq['same']}")
