# mono

> Mono, the open source development platform based on the .NET Framework.
> More information: <https://www.mono-project.com/docs/>.

- Compile:

`csc {{source_file}}.cs`

- Run:

`mono {{source_file}}.exe`

- Compile using a specific library:

`csc {{source_file}}.cs -r:{{specific_library}}.dll`

- Compile with mcs and pull in library as package:

`mcs {{source_file}}.cs -pkg:{{package}}`
