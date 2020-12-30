release:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
.PHONY: release

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
.PHONY: clean

