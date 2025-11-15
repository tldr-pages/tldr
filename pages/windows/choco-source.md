# choco source

> Manage sources for packages with Chocolatey.
> More information: <https://chocolatey.org/docs/commands-source>.

- List currently available sources:

`choco source list`

- Add a new package source:

`choco source add {{[-n|--name]}} {{name}} {{[-s|--source]}} {{url}}`

- Add a new package source with credentials:

`choco source add {{[-n|--name]}} {{name}} {{[-s|--source]}} {{url}} {{[-u|--user]}} {{username}} {{[-p|--password]}} {{password}}`

- Add a new package source with a client certificate:

`choco source add {{[-n|--name]}} {{name}} {{[-s|--source]}} {{url}} --cert {{path\to\certificate_file}}`

- Enable a package source:

`choco source enable {{[-n|--name]}} {{name}}`

- Disable a package source:

`choco source disable {{[-n|--name]}} {{name}}`

- Remove a package source:

`choco source remove {{[-n|--name]}} {{name}}`
