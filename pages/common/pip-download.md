# pip download

> Download Python packages without installing them.
> More information: <https://pip.pypa.io/en/stable/cli/pip_download/>.

- Download a package wheel or source archive to the current directory:

`pip download {{package}}`

- Download a specific version of a package:

`pip download {{package}}=={{version}}`

- Download a package and its dependencies to a specific directory:

`pip download {{package}} {{[-d|--dest]}} {{path/to/directory}}`

- Download a package for a specific platform and Python version:

`pip download {{package}} --only-binary :all: --platform {{platform}} --python-version {{version}}`

- Download a package from a specific index URL:

`pip download {{package}} {{[-i|--index-url]}} {{url}}`
