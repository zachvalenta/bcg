.PHONY: test

help:
	@echo
	@echo "🍶 FLASK"
	@echo
	@echo "flask:       start app"
	@echo "home:        open homepage"
	@echo "get:         GET quote on first pet"
	@echo
	@echo "🛠  DB UTILS"
	@echo
	@echo "seed:        seed db"
	@echo "shell:       open db REPL"
	@echo
	@echo "📊 CODE QUALITY"
	@echo
	@echo "test:        run unit tests"
	@echo "cov:         view coverage report"
	@echo "lint:        lint using flake8"
	@echo "fmt:         format using black"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "freeze:      freeze dependencies into requirements.txt"
	@echo "install:     install dependencies from requirements.txt"
	@echo "purge:       remove any installed pkg *not* in requirements.txt"
	@echo

#
# FLASK
#

flask:
	source venv/bin/activate; flask run

home:
	open http://localhost:5000

get:seed
	http http://localhost:5000/pet?id=1

#
# DB UTILS
#

seed:
	rm local.db; source venv/bin/activate; python db_seed.py

shell:
	source venv/bin/activate; bpython -i db_shell.py

#
# CODE QUALITY
#

test:
	coverage run --source='app' -m pytest -v app_test.py && coverage report -m

cov:
	coverage html; open htmlcov/index.html

lint:
	flake8 --ignore=E402 --per-file-ignores='db_shell.py:F401' app.py app_test.py models.py db_seed.py db_shell.py

fmt:
	black app.py app_test.py models.py db_seed.py db_shell.py

#
# DEPENDENCIES
#

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

purge:
	@echo "🔍 - DISCOVERING UNSAVED PACKAGES\n"
	pip freeze > pkgs-to-rm.txt
	@echo
	@echo "📦 - UNINSTALL ALL PACKAGES\n"
	pip uninstall -y -r pkgs-to-rm.txt
	@echo
	@echo "♻️  - REINSTALL SAVED PACKAGES\n"
	pip install -r requirements.txt
	@echo
	@echo "🗑  - UNSAVED PACKAGES REMOVED\n"
	diff pkgs-to-rm.txt requirements.txt | grep '<'
	@echo
	rm pkgs-to-rm.txt
	@echo
