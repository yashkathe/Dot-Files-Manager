# Dotfile Manager

A simple script to **sync dotfiles and directories** to a central *emit_folder* for backup or management.

## Features

- Detects and copies **new** or **changed** dotfiles
- Syncs entire **directories** if missing
- Smart file comparison (uses hashes)
- Logs with stats after sync

## Usage

1. Create a `config.json`:

   ```text
   {
    // files and directories you want to track
    "dot_files": {
        "directories": [],
        "files": []
    },
    // where the dot files should be emitted
    "emit_folder": "/home/yashkathe/dot_files_manager",
    // github repository where dot files should be pushed
    "git-repository": ""
    }
   ```

2. Run:

   ```bash
   
   python3 src/dot_files_manager/main.py
   ```
![output image](docs/output.png)