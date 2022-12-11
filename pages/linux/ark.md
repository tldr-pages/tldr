# ark

> KDE's archiving tool.
> More information: <https://docs.kde.org/stable5/en/ark/ark/>.

- Extract a specific archive into the current directory:

`ark --batch {{path/to/archive}}`

- Extract an archive into a specific directory:

`ark --batch --destination {{path/to/directory}} {{path/to/archive}}`

- Create an archive if it does not exist and add specific files to it:

`ark --add-to {{path/to/archive}} {{path/to/file1 path/to/file2 ...}}`
