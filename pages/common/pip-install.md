# pip install

> Install Python packages.
> More information: <https://pip.pypa.io>.

- Install a package:

`pip install {{package}}`

- Install a specific version of a package:

`pip install {{package}}=={{version}}`

- Install packages listed in a file:

`pip install -r {{path/to/requirements.txt}}`

- Install packages from an URL or local file archive (.tar.gz | .whl):

`pip install --find-links {{url|path/to/file}}`

- Install the local package in the current directory in develop (editable) mode:

`pip install --editable {{.}}`
