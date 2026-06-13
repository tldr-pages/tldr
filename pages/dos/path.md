# PATH

> Display or set the search path for executable files.
> This command is available in `FreeDOS` only.
> More information: <https://help.fdos.org/en/hhstndrd/batch/path.htm>.

- Display the current search path:

`PATH`

- Set the semicolon-separated list of directories to search in:

`PATH {{path/to/directory1;path/to/directory2;...}}`

- Append a directory to the search path:

`PATH %PATH%;{{path/to/directory}}`

- Add a directory to the beginning of the search path:

`PATH {{path/to/directory}};%PATH%`

- Clear the search path:

`PATH;`

- Display help:

`PATH /?`
