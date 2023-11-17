# choco pack

> Package a NuGet specification into a `nupkg` file.
> More information: <https://chocolatey.org/docs/commands-pack>.

- Package a NuGet specification to a `nupkg` file:

`choco pack {{path\to\specification_file}}`

- Package a NuGet specification specifying the version of the resulting file:

`choco pack {{path\to\specification_file}} --version {{version}}`

- Package a NuGet specification to a specific directory:

`choco pack {{path\to\specification_file}} --output-directory {{path\to\output_directory}}`
