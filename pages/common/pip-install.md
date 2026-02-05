# pip install

> Install Python packages.
> More information: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Install one or more packages:

`pip install {{package1 package2 ...}}`

- Upgrade all specified packages to the latest version, installing any that are not already present:

`pip install {{package1 package2 ...}} {{[-U|--upgrade]}}`

- Install a specific version of a package:

`pip install {{package}}=={{version}}`

- Install packages listed in a file:

`pip install {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Install a package from a local archive or directory:

`pip install {{path/to/file.whl|path/to/file.tar.gz|path/to/directory}}`

- Install a package from a Git repository:

`pip install git+https://{{example.com}}/{{user}}/{{repository}}.git`

- Install a package from an alternative source (URL or directory) instead of PyPI:

`pip install {{[-f|--find-links]}} {{url|path/to/directory}} {{package}}`

- Install the local package in the current directory in develop (editable) mode:

`pip install {{[-e|--editable]}} .`
