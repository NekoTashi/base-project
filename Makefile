init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

run:
	python manage.py runserver_plus

shell:
	python manage.py shell_plus

cove:
	coverage run manage.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

test:
	pipenv run pytest --cov-report term --cov=v1

clean:
	rm -rf .tox/
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache

.PHONY: init run shell cove test clean
