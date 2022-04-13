# rm

> Removes files or directories.
> See also: `rmdir`.
> More information: <https://www.gnu.org/software/coreutils/rm>.

- Remove specific files:

`rm {{path/to/file{1,2,...} }}`

- Remove specific files ignoring nonexistent ones:

`rm --force {{path/to/file{1,2,...} }}`

- Remove specific files interactively prompting before each removal:

`rm --interactive {{path/to/file{1,2,...} }}`

- Remove specific files printing info about each removal:

`rm --verbose {{path/to/file{1,2,...} }}`

- Remove specific files/directories [r]ecursively:

`rm --recursive {{path/to/file_or_directory{1,2,...} }}`
