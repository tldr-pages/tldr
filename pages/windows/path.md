# path

> Display or set the search path for executable files.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- Display the current path:

`path`

- Set the path to one or more semicolon-separated directories:

`path {{path/to/directory(s)}}`

- Append a new directory to the original path:

`path {{path/to/directory}};%path%`

- Set command prompt to only search the current directory for executables:

`path ;`
