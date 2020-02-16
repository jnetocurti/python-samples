ENV_HOME:=.venv
PYTHON_VERSION:=3.6.5
BOLD:=$(shell tput bold)
RESET:=$(shell tput sgr0)
GREEN:=$(shell tput setaf 2)

SUCCESS_MESSAGE:=OK
SUCCESS:=$(GREEN)$(SUCCESS_MESSAGE)$(RESET)
SEPARATOR:=---------------------------------------------------------

help:
	@echo "$(BOLD)destroy$(RESET): - Remove the environment"
	@echo "$(BOLD)create$(RESET):  - Create the environment"
	@echo "$(BOLD)lint$(RESET):    - Run flake8 lint"
	@echo "$(BOLD)test$(RESET):    - Run all tests"

destroy:
	@echo "Destroing the virtual environment ..."
	@rm -R $(ENV_HOME)
	@echo "$(SUCCESS)"

create:
	@echo "Creating the environment ..."
	@python -m venv $(ENV_HOME)
	@echo "$(SUCCESS)"

	@echo "Installing dependencies ..."
	@.venv/bin/pip install -q --no-cache-dir -r requirements.txt
	@echo "$(SUCCESS)"

	@echo $(SEPARATOR)
	@echo "Everything is ready, type it to activate the environment!"
	@echo ""
	@echo "source $(ENV_HOME)/bin/activate"
	@echo $(SEPARATOR)

lint:
	@$(ENV_HOME)/bin/flake8 --show-source ./src ./test

test: lint
	@$(ENV_HOME)/bin/pytest
