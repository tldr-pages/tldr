# pip install

> Install Python packages.
> More information: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Install one or more packages:

`pip install {{package1|path/to/package1 package2|path/to/package2 ...}}`

- Upgrade all specified packages to the latest version, installing any that are not already present:

`pip install {{package1 package2 ...}} {{[-U|--upgrade]}}`

- Install a specific version of a package:

`pip install {{package}}=={{version}}`

- Install packages listed in a file:

`pip install {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Install packages from a URL:

`pip install {{[-f|--find-links]}} {{url}}`

- Install the local package in the current directory in develop (editable) mode:

`pip install {{[-e|--editable]}} .`
