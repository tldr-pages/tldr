# cp

> Copy files and folders.

- Copy a file to another location:

`cp {{path/to/file.ext}} {{path/to/copy.ext}}`

- Copy a file into another folder, keeping the filename:

`cp {{path/to/file.ext}} {{path/to/target/parent/folder}}`

- Copy a folder recursively to another location:

`cp -r {{path/to/folder}} {{path/to/copy}}`

- Copy a folder recursively into another folder, keeping the folder name:

`cp -r {{path/to/folder}} {{path/to/target/parent/folder}}`

- Copy a folder recursively, in verbose mode (shows files as they are copied):

`cp -vr {{path/to/folder}} {{path/to/copy}}`

- Copy the contents of a folder into another folder:

`cp -r {{path/to/source/folder/*}} {{path/to/target/folder}}`

- Copy text files to another location, in interactive mode (prompts user before overwriting):

`cp -i {{*.txt}} {{path/to/source/}}`
