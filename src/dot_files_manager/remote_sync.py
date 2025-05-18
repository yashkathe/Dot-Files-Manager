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


# safe git push with atomic transaction
def safe_git_push():

    curr_head = None

    try:
        commit_hash = create_hash()

        # get branch-name
        p2 = subprocess.run(
            "git rev-parse --abbrev-ref HEAD",
            capture_output=True,
            text=True,
            shell=True,
        )
        branch = p2.stdout.strip()

        # get current head
        p3 = subprocess.run(
            "git rev-parse HEAD", capture_output=True, text=True, shell=True
        )
        curr_head = p3.stdout.strip()

        # sync repository
        p4 = subprocess.run("git add .", shell=True, capture_output=True, text=True)
        if p4.returncode != 0:
            raise RuntimeError(p4.stderr)

        p5 = subprocess.run(
            f"git commit -m 'sync {commit_hash}'",
            shell=True,
            capture_output=True,
            text=True,
        )
        if p5.returncode != 0:
            raise RuntimeError(p5.stderr)

        p6 = subprocess.run(
            f"git push origin {branch}", shell=True, capture_output=True, text=True
        )
        print(p6.returncode)
        if p6.returncode != 0:
            raise RuntimeError(p6.stderr)

    except KeyboardInterrupt:
        print("Interrupted by user during git operation.")
        if curr_head:
            subprocess.run(f"git reset --hard {curr_head}", shell=True)
            print("rolled back git changes")
        sys.exit(130)

    except Exception as e:
        print(f"error: {e}")
        if curr_head:
            subprocess.run(f"git reset --hard {curr_head}", shell=True)
            print("rolled back git changes")
        sys.exit(1)


# sync emit directory with `git`
def remote_sync(conf_file):

    with open(conf_file, "r") as rf:

        load_conf = json.load(rf)

        emit_dir = load_conf["emit_folder"]

    os.chdir(emit_dir)

    p1 = subprocess.run("git status", shell=True, capture_output=True)

    if p1.returncode != 0:
        print(p1.stderr)
        sys.exit(1)

    if "working tree clean" in str(p1.stdout):
        print("Remote Directory up to Date")
        sys.exit(0)

    safe_git_push()
    return 0
