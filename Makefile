lock:
	@pip-compile --upgrade -o requirements.txt
	@pip-compile --extra dev --upgrade -o requirements-dev.txt

sync:
	@pip-sync requirements.txt

sync-dev:
	@pip-sync requirements-dev.txt

fmt:
	@isort .
	@black .

lint:
	@mypy app
	@flake8 app
	@bandit -c pyproject.toml --silent -r app
