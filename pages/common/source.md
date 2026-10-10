# source

> Execute commands from a file in the current shell.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-source>.

- Evaluate contents of a given file:

`source {{path/to/file}}`

- Evaluate a file with arguments:

`source {{path/to/file}} {{argument1 argument2 ...}}`

- Search and evaluate a file from `$PATH`:

`source {{file}}`

- Search and evaluate a file in a given set of directories:

`source -p {{path/to/directory1:path/to/directory2:...}} {{file}}`

- Evaluate contents of a given file (alternatively replacing `source` with `.`):

`. {{path/to/file}}`
