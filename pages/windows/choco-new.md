# choco new

> Generate new package specification files with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/create/commands/new>.

- Create the new package skeleton:

`choco new {{package_name}}`

- Create the new package with the specified version:

`choco new {{package_name}} --version {{package_version}}`

- Create the new package with the specified maintainer name:

`choco new {{package_name}} --maintainer {{maintainer_name}}`

- Create the new package in the specified output directory:

`choco new {{package_name}} --output-directory {{path/to/directory}}`

- Create the new package with specific 32-bit and 64-bit installer URLs:

`choco new {{package_name}} url="{{url}}" url64="{{url}}"`
