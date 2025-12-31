# ark

> KDE's archiving tool.
> More information: <https://docs.kde.org/stable5/en/ark/ark/>.

- Extract a specific archive into the current directory:

`ark {{[-b|--batch]}} {{path/to/archive}}`

- Extract an archive into a specific directory:

`ark {{[-b|--batch]}} {{[-o|--destination]}} {{path/to/directory}} {{path/to/archive}}`

- Create an archive if it does not exist and add specific files to it:

`ark {{[-t|--add-to]}} {{path/to/archive}} {{path/to/file1 path/to/file2 ...}}`
