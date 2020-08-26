# ark

> KDE archiving tool.
> More information: <https://docs.kde.org/stable5/en/kdeutils/ark/>.

- Extract an archive into the current directory:

`ark --batch {{archive}}`

- Change extraction directory:

`ark --batch --destination {{path/to/directory}} {{archive}}`

- Create an archive if it does not exist and add files to it:

`ark --add-to {{archive}} {{file1}} {{file2}}`
