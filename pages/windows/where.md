# where

> Display the location of files that match the search pattern.
> Defaults to current work directory and paths in the PATH environment variable.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- Display the location of file pattern:

`where {{path/to/file}}`

- Display the location of file pattern including file size and date:

`where /T {{path/to/file}}`

- Recursively search for file pattern at specified path:

`where /R {{path/to/directory}} {{path/to/file}}`

- Silently return the error code for the location of the file pattern:

`where /Q {{path/to/file}}`
