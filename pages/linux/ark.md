# ark

> KDE archiving tool.
> More information: <https://docs.kde.org/stable5/en/kdeutils/ark/index.html>.

- Extract archive in current directory:

`ark --batch {{archive}}`

- Change extraction directory:

`ark --batch --destination {{path/to/directory}} {{archive}}`

- Create archive if it does not exist and add files to it:

`ark --add-to {{archive}} {{file1}} {{file2}}`
