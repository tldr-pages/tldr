# pip

> Python package manager.
> Some subcommands such as `pip install` have their own usage documentation.
> More information: <https://pip.pypa.io>.

- Install a package (see `pip install` for more install examples):

`pip install {{package_name}}`


- Install a specific version of a package:

`pip install {{package}}=={{version}}`

- Upgrade a package:

`pip install -U {{package_name}}`

- Uninstall a package:

`pip uninstall {{package_name}}`

- Save installed packages to file:

`pip freeze > {{requirements.txt}}`

- Install packages from a file:

`pip install --requirement {{requirements.txt}}`

- Show installed package info:

`pip show {{package_name}}`
