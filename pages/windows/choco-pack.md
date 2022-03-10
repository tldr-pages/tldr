# choco pack

> Package a NuGet specification into a nupkg file.
> More information: <https://docs.chocolatey.org/en-us/create/commands/pack>.

- Package the NuGet specification to the specified nupkg file:

`choco pack {{path/to/specification}}`

- Package the NuGet specification specifying the version of the resulting file:

`choco pack {{path/to/specification}} --version {{specification_version}}`

- Package the NuGet specification to the specified directory:

`choco pack {{path/to/specification}} --output-directory {{path/to/directory}}`
