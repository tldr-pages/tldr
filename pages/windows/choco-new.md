# choco new

> Generate new package specification files with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/create/commands/new>.

- Create a new package skeleton:

`choco new {{package_name}}`

- Create a new package with the specified version:

`choco new {{package_name}} --version {{package_version}}`

- Create a new package with the specified maintainer name:

`choco new {{package_name}} --maintainer {{maintainer_name}}`

- Create a new package in the specified output directory:

`choco new {{package_name}} --output-directory {{path/to/directory}}`

- Create a new package with specific 32-bit and 64-bit installer URLs:

`choco new {{package_name}} url="{{url}}" url64="{{url}}"`
