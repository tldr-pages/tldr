# choco pack

> Package a NuGet specification into a nupkg file.
> More information: <https://docs.chocolatey.org/en-us/create/commands/pack>.

- Package a NuGet specification to a specified nupkg file:

`choco pack {{path/to/specification}}`

- Package a NuGet specification specifying the version of the resulting file:

`choco pack {{path/to/specification}} --version {{specification_version}}`

- Package a NuGet specification to a specified directory:

`choco pack {{path/to/specification}} --output-directory {{path/to/directory}}`
