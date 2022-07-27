#Makefile
	
.PHONY: run clean
setup:
	pip3 install -r requirements.txt

clean:
	rm -rf __pycache__

run:
	.\main.py


