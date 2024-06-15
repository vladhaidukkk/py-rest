default: fmt lint

fmt:
	ruff format app

lint:
	mypy app
	ruff check app
