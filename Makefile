.PHONY: run install

run:
	python3 -m src.dot_files_manager.main

install:
	pip install -r requirements.txt
	if [ ! -f d_manager.json ]; then cp d_manager.copy.json d_manager.json; fi
