# Dotfiles Manager

A simple script to **sync dotfiles and directories** to a central *emit_folder* for backup or management.

<div align="center">

![GitHub license](https://img.shields.io/github/license/yashkathe/Dot-Files-Manager)
![GitHub repo size](https://img.shields.io/github/repo-size/yashkathe/Dot-Files-Manager)
![GitHub last commit](https://img.shields.io/github/last-commit/yashkathe/Dot-Files-Manager)
![GitHub issues](https://img.shields.io/github/issues/yashkathe/Dot-Files-Manager)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yashkathe/Dot-Files-Manager)
<!-- ![GitHub stars](https://img.shields.io/github/stars/yashkathe/Dot-Files-Manager?style=social) -->

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
make run
```

---

Everytime you change a dot file you can just run make run to sync that dot file with emit directory
