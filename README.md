# Dotfiles Manager

<div align="center">

A simple script to **sync dotfiles and directories** to a central _emit_folder_ for backup or management.

![GitHub license](https://img.shields.io/github/license/yashkathe/Dot-Files-Manager)
![GitHub repo size](https://img.shields.io/github/repo-size/yashkathe/Dot-Files-Manager)
![Platform linux](https://img.shields.io/badge/platform-Linux-important)
![Top Language](https://img.shields.io/github/languages/top/yashkathe/Dot-Files-Manager)

</div>

<div align="center">

![GitHub issues](https://img.shields.io/github/issues/yashkathe/Dot-Files-Manager)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yashkathe/Dot-Files-Manager)
![GitHub last commit](https://img.shields.io/github/last-commit/yashkathe/Dot-Files-Manager)

<img src="docs/output.png" alt="output image" width="650"/>

</div>

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yashkathe/Dot-Files-Manager.git
```

### 2. Installation

```bash
make install
```

### 3. Populate d_manager.json

```bash
make run ARGS=-e # edit the config file
```

```text
"dot_files": {
        "directories": [
            *path of directories to track*
        ],
        "files": [
            *path of files to track*
        ]
    },
    "emit_folder": *path of directory where all dot files & directories should be colleced*,
```

### 4. Execute

```bash
make run ARGS=-r # run the main file
```

### HELP

```bash
make run ARGS=-h # program manual
```

---

Everytime you update a dot file / config file you can just run **_make run_** to sync all dot files with your emit directory
