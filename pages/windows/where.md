# where

> Display the location of files that match the search pattern.
> Defaults to current work directory and paths in the PATH environment variable.

- Display the location of file pattern:

`where {{file_pattern}}`

- Display the location of file pattern including file size and date:

`where /T {{file_pattern}}`

- Recursively search for file pattern at specified path:

`where /R {{path/to/directory}} {{file_pattern}}`

- Display only the error code for the location of file pattern:

`where /Q {{file_pattern}}`
