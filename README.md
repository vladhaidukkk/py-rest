# SOAP API example with Python

## Packages Management

We use two types of software packages: ones needed for the software to work, and ones that make it easier to build the
software. All these are listed in a file named `pyproject.toml`.

### Add a New Dependency

If you need to add a new dependency that's important for the software to work, add it to the `dependencies` list
in `pyproject.toml`. If the dependency is just to help make the software, add it to the `dev` list in
the `optional-dependencies` section.

### Keep Track of Dependencies

We use a tool called `pip-tools` to keep all our dependencies organized. To install it on your computer, type this
command:

```shell
pip install pip-tools
```

You can find a bunch of helpful commands in the `Makefile`, including ones that help manage our dependencies. Here's a
brief overview of them:

- `lock` - locks versions of all dependencies listed in `pyproject.toml`. Thanks to the `--upgrade` option, it doesn't
  overwrite already locked dependencies, it just creates new ones.
- `sync` - installs missing dependencies and removes redundant ones.
- `sync-dev` - do the same as `sync`, but also takes into account dev dependencies.

## Code Style

We use [Black](https://black.readthedocs.io/en/stable/) to automatically format code according
to [PEP8](https://peps.python.org/pep-0008/). For imports ordering we use [isort](https://pycqa.github.io/isort/). Both
tools are configured in `pyproject.toml` to be compatible with each other.

To run them both at the same time and in the correct order, you can use the `fmt` command from the `Makefile`.

To disable formatting for a specific line of code, append `# fmt: skip`
for [Black](https://black.readthedocs.io/en/stable/) or `# isort: skip` for [isort](https://pycqa.github.io/isort/).
These comments tell the formatters to skip the respective lines. If you want to combine them both into one line,
separate them with a semicolon: `# fmt: skip; isort: skip`.
