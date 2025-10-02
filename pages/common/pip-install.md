# pip install

> Install Python packages.
> More information: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Install a package:

`pip install {{package}}`

- Install a specific version of a package:

`pip install {{package}}=={{version}}`

- Install packages listed in a file:

`pip install {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Install packages from an URL or local file archive (e.g. `.tar.gz`, `.whl`):

`pip install {{[-f|--find-links]}} {{url|path/to/file}}`

- Install the local package in the current directory in develop (editable) mode:

`pip install {{[-e|--editable]}} .`
