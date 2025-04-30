.PHONY: run install

run sync:
	python3 -m src.dot_files_manager.main --run

edit:
	python3 -m src.dot_files_manager.main --edit

help:
	python3 -m src.dot_files_manager.main --help

install:
	pip3 install -r requirements.txt
	if [ ! -f d_manager.json ]; then cp d_manager.copy.json d_manager.json; fi
