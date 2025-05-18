import hashlib
import json
import os
import subprocess
import sys
import time


# create hash for commit history using `epoch_time`
def create_hash():

    curr_time = int(time.time())  # epoch time
    hash = hashlib.sha256(str(curr_time).encode())

    return hash.hexdigest()


# sync emit directory with `git`
def remote_sync(conf_file):

    with open(conf_file, "r") as rf:

        load_conf = json.load(rf)

        emit_dir = load_conf["emit_folder"]
        # git_repo = load_conf["git_repository"]

    os.chdir(emit_dir)

    p1 = subprocess.run("git status", shell=True, capture_output=True)

    if p1.returncode != 0:
        print(p1.stderr)
        sys.exit(1)

    if "working tree clean" in str(p1.stdout):
        print("Remote Directory up to Date")
        sys.exit(0)

    commit_hash = create_hash()

    # get branch-name
    p2 = subprocess.run(
        "git rev-parse --abbrev-ref HEAD",
        capture_output=True,
        text=True,
        shell=True,
    )
    branch = p2.stdout

    # sync repository
    subprocess.run("git add .", shell=True)
    subprocess.run(f"git commit -m 'sync {commit_hash}'", shell=True)
    subprocess.run(f"git push origin {branch}", shell=True)

    return 0
