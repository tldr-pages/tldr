# ln

> Creates links to files and folders

- create a symbolic link to a file or folder

`ln -s {{path/to/original/file}} {{path/to/link}}`

- overwrite a symbolic link to a file

`ln -sf {{path/to/new/original/file}} {{path/to/file/link}}`

- overwrite a symbolic link to a folder

`ln -sfT {{path/to/new/original/file}} {{path/to/folder/link}}`

- create a hard link to a file or folder

`ln {{path/to/original/file}} {{path/to/link}}`
