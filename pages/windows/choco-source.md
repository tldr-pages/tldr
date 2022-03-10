# choco source

> Manage sources for packages with Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/source>.

- Print all currently available sources:

`choco source list`

- Add the new package source:

`choco source add --name {{source_alias}} --source {{source_url}}`

- Add the new package source with the specified credentials:

`choco source add --name {{source_alias}} --source {{source_url}} --user {{username}} --password {{password}}`

- Add the new package source with the specified client certificate:

`choco source add --name {{source_alias}} --source {{source_url}} --cert {{path/to/certificate}}`

- Enable/disable the specified package source:

`choco source {{enable|disable}} --name {{source_alias}}`

- Remove the specified package source:

`choco source remove --name {{source_alias}}`
