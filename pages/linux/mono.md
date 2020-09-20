# mono

> Runtime for the .NET Framework.
> More information: <https://www.mono-project.com/docs/>.

- Compile:

`csc {{source_file}}.cs`

- Run a .NET assembly in debug mode:

`mono --debug {{path/to/source_file}}.exe`

- Compile using a specific library:

`csc {{source_file}}.cs -r:{{specific_library}}.dll`

- Compile with mcs and pull in library as package:

`mcs {{source_file}}.cs -pkg:{{package}}`
