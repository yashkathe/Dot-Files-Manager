.PHONY: run install

run sync:
	python3 -m src.dot_files_manager.main --run

remote-sync:
	python3 -m src.dot_files_manager.main --remote-sync

full-sync:
	python3 -m src.dot_files_manager.main --run
	python3 -m src.dot_files_manager.main --remote-sync

edit:
	python3 -m src.dot_files_manager.main --edit

help:
	python3 -m src.dot_files_manager.main --help

install:
	pip3 install -r requirements.txt
	if [ ! -f d_manager.json ]; then cp d_manager.copy.json d_manager.json; fi
