# SOAP API example with Python

## Packages Management

We use two types of software packages: ones needed for the software to work, and ones that make it easier to build the software. All these are listed in a file named `pyproject.toml`.

### Add a New Dependency

If you need to add a new dependency that's important for the software to work, add it to the `dependencies` list in `pyproject.toml`. If the dependency is just to help make the software, add it to the `dev` list in the `optional-dependencies` section.

### Keep Track of Dependencies

We use a tool called `pip-tools` to keep all our dependencies organized. To install it on your computer, type this command:

```shell
pip install pip-tools
```

You can find a bunch of helpful commands in the `Makefile`, including ones that help manage our dependencies. Here's a brief overview of them:

- `lock` - locks versions of all dependencies listed in `pyproject.toml`. Thanks to the `--upgrade` option, it doesn't overwrite already locked dependencies, it just creates new ones.
- `sync` - installs missing dependencies and removes redundant ones.
- `sync-dev` - do the same as `sync`, but also takes into account dev dependencies.
