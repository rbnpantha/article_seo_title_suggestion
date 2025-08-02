# Makefile for News Title and SEO Tag Generator

.PHONY: help install run clean

help:
	@echo "Usage:"
	@echo "  make install   - Install required Python packages"
	@echo "  make run       - Run the main script"
	@echo "  make clean     - Remove generated output file"

install:
	pip install -r requirements.txt

run:
	python main.py

clean:
	rm -f output.txt
