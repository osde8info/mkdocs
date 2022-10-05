SHELL:=/bin/bash

install:
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip3 install -r requirements.txt

serve:
	source venv/bin/activate && mkdocs serve
