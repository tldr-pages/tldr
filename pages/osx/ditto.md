# ditto

> Copy files and folders

- Overwrites contents of destination folder with contents of source folder

`ditto {{path/to/source}} {{path/to/destination}}`

- print a line to the Terminal window for every file that’s being copied

`ditto -V {{path/to/source}} {{path/to/destination}}`

- copy a given file or folder, while retaining the original file permissions.

`ditto -rsrc {{path/to/source}} {{path/to/destination}}`
