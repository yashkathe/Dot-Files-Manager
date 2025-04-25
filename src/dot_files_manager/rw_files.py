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
            "Emit Directory Not Found in Config File"
            return 1

        # check if dot files exist
        if not load_conf["dot_files"]["files"]:
            print(f"no dot files regiesterd in {conf_file}")
            return 0

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

def check_folder_diff(conf_file):

    with open(conf_file, "r") as rf:
        load_conf = json.load(rf)
        emit_dir = load_conf["emit_folder"]

        if not emit_dir:
            print("Emit Directory Not Found in Config File")
            return 1

        dirs = load_conf["dot_files"].get("directories", [])
        if not dirs:
            print(f"no directories registered in {conf_file}")
            return 0

        print(f"\nStarting to Sync dot-directories from {conf_file}\n")
        dir_freq = defaultdict(int)
        freq = defaultdict(int)  # keys: new, change, same, deleted

        for src_dir in dirs:
            if os.path.exists(src_dir):
                dir_freq["total"] += 1
                dir_name = os.path.basename(src_dir)
                target_dir = os.path.join(emit_dir, dir_name)

                # If the whole directory is missing, copy it wholesale
                if not os.path.exists(target_dir):
                    print(f"new directory detected -> {dir_name}")
                    cp = subprocess.run(
                        f"cp -r {src_dir} {emit_dir}",
                        shell=True,
                        capture_output=True,
                        text=True,
                    )
                    if cp.returncode != 0:
                        print(cp.stderr)
                    dir_freq["new"] += 1
                    continue
                else:
                    dir_freq["existing"] += 1

                # 1) Sync files from source -> emit
                for root, _, files in os.walk(src_dir):
                    for file_name in files:
                        src_path = os.path.join(root, file_name)
                        rel = os.path.relpath(root, src_dir)
                        emit_sub = os.path.join(target_dir, rel)
                        emit_path = os.path.join(emit_sub, file_name)

                        os.makedirs(emit_sub, exist_ok=True)

                        if not os.path.exists(emit_path):
                            print(f"new file detected -> {os.path.relpath(emit_path, emit_dir)}")
                            copy_files(src_path, emit_path)
                            freq["new"] += 1
                        elif not are_similar_files(src_path, emit_path):
                            print(f"changes detected -> {os.path.relpath(emit_path, emit_dir)}")
                            copy_files(src_path, emit_path)
                            freq["change"] += 1
                        else:
                            freq["same"] += 1

                # 2) Detect & remove files that no longer exist in source
                for root, _, files in os.walk(target_dir):
                    for file_name in files:
                        emit_path = os.path.join(root, file_name)
                        rel = os.path.relpath(emit_path, target_dir)
                        src_path = os.path.join(src_dir, rel)
                        if not os.path.exists(src_path):
                            print(f"deleted file detected -> {os.path.relpath(emit_path, emit_dir)}")
                            try:
                                os.remove(emit_path)
                                freq["deleted"] += 1
                            except OSError as e:
                                print(f"error deleting {emit_path}: {e}")
            else:
                print(f"{src_dir} not found")

    # final summary
    total_files = sum(freq[k] for k in ("new", "change", "same", "deleted"))
    print("\n=========================================")
    print(f"📂 Total Directories Processed: {dir_freq['total']}")
    print(f"└─✨ New Directories: {dir_freq['new']}")
    print(f"└─✨ Existing Directories: {dir_freq['existing']}")
    print(f"✅ Total Files Scanned: {total_files}")
    print(f"└─✨ New Files: {freq['new']}")
    print(f"└─✨ Re-uploaded Files: {freq['change']}")
    print(f"└─✨ Un-touched Files: {freq['same']}")
    print(f"└─✨ Deleted Files: {freq['deleted']}")
    print("=========================================\n")
