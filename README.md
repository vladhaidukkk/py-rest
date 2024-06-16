# Rest API example with Python

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## Table of Contents

- [Dependencies Management](#dependencies-management)
- [Code Formatting & Linting](#code-formatting--linting)
- [Type Checking](#type-checking)
- [Git Hooks](#git-hooks)
    - [Getting Started](#getting-started)
    - [Configuration](#configuration)

## Dependencies Management

We manage our project dependencies using [Poetry](https://python-poetry.org/), a robust tool designed to simplify
package management and dependency resolution in Python projects.

For detailed guidance on installing and using Poetry, refer to
the [official documentation](https://python-poetry.org/docs/). The documentation is well-organized and easy to follow,
providing clear instructions for both beginner and advanced users.

## Code Formatting & Linting

We use [Ruff](https://docs.astral.sh/ruff/), an all-in-one tool for code formatting and linting. Built
with [Rust](https://www.rust-lang.org/), Ruff delivers exceptional performance, capable of analyzing code in
milliseconds, which markedly outpaces traditional Python-based tools
like [Black](https://black.readthedocs.io/en/stable/) and [Flake8](https://flake8.pycqa.org/en/latest/) by 100 to 300
times.

In the `Makefile` you can find commands to format and lint your code.

## Type Checking

We use [mypy](http://mypy-lang.org/) for type checking in our Python projects. Mypy is a static type checker that helps
catch type errors at compile time, significantly enhancing code reliability and maintainability.

## Git Hooks

We use [pre-commit](https://pre-commit.com) for managing Git hooks. The main use is the `pre-commit` hook, which
checks the style of the code before making a commit. This helps to make sure that code reviews are simpler and free from
style issues.

### Getting Started

To set up Git hooks in your local repository, type:

```shell
pre-commit install
```

If for some reason you need to remove them from the `.git/hooks` directory, type:

```shell
pre-commit uninstall
```

> **IMPORTANT**: Set up pre-commit once in your local environment and forget about it.

### Configuration

Although pre-commit can be used with various programming languages, we mainly use it for Python, for which it was
originally created.

Our configuration is in the `.pre-commit-config.yaml` file. We currently
use [local hooks](https://pre-commit.com/#repository-local-hooks), but the real power
of pre-commit is being able to use tools without having to install them on your machine. To understand more about this,
take a look at this [guide](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project). Also, check out the full
list of available third-party repos with hooks [here](https://pre-commit.com/hooks.html).

### Managing and Testing Hooks

To check if your configuration is correct, use:

```shell
pre-commit validate-config
```

To update your hook repositories to the latest versions, use:

```shell
pre-commit autoupdate
```

If you need to update a specific repository:

```shell
pre-commit autoupdate --repo <repo>
```

You don't need to make a test commit to see if a hook works. Instead, you can run:

```shell
pre-commit run --all-files
```

Or, to test a specific hook:

```shell
pre-commit run <hook_id> --all-files
```
