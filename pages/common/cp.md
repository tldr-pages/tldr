# cp

> Copy files and directories.

- Copy a file to another location:

`cp {{path/to/file.ext}} {{path/to/copy.ext}}`

- Copy a file into another directory, keeping the filename:

`cp {{path/to/file.ext}} {{path/to/target_parent_directory}}`

- Copy a directory recursively to another location:

`cp -r {{path/to/directory}} {{path/to/copy}}`

- Copy a directory recursively, in verbose mode (shows files as they are copied):

`cp -vr {{path/to/directory}} {{path/to/copy}}`

- Copy the contents of a directory into another directory:

`cp -r {{path/to/source_directory/*}} {{path/to/target_directory}}`

- Copy text files to another location, in interactive mode (prompts user before overwriting):

`cp -i {{*.txt}} {{path/to/target_directory}}`
