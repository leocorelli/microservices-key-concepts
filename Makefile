install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_logic.py test_main.py

format:
	black *.py

lint:
	pylint --disable=R,C logic.py

all: install lint