# choco new

> Generate new package specification files with Chocolatey.
> More information: <https://chocolatey.org/docs/commands-new>.

- Create a new package skeleton:

`choco new {{package}}`

- Create a new package with a specific version:

`choco new {{package}} --version {{version}}`

- Create a new package with a specific maintainer name:

`choco new {{package}} --maintainer {{maintainer_name}}`

- Create a new package in a custom output directory:

`choco new {{package}} --output-directory {{path/to/directory}}`

- Create a new package with specific 32-bit and 64-bit installer URLs:

`choco new {{package}} url="{{url}}" url64="{{url}}"`
