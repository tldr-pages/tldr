# pip

> Python package manager.
> Some subcommands such as `install` have their own usage documentation.
> More information: <https://pip.pypa.io/en/stable/cli/pip/>.

- Install a package (see `pip install` for more install examples):

`pip install {{package}}`

- Install a package to the user's directory instead of the system-wide default location:

`pip install --user {{package}}`

- Upgrade a package:

`pip install {{[-U|--upgrade]}} {{package}}`

- Uninstall a package:

`pip uninstall {{package}}`

- Save installed packages to file:

`pip freeze > {{requirements.txt}}`

- List installed packages:

`pip list`

- Show installed package info:

`pip show {{package}}`

- Install packages from a file:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
