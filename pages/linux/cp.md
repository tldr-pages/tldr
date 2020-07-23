# cp

> Copy files and directories.

- Copy a file to another location:

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- Copy a file into another directory, keeping the filename:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- Recursively copy a directory's contents to another location (if the destination exists, the directory is copied inside it):

`cp -r {{path/to/source_directory}} {{path/to/target_directory}}`

- Copy a directory recursively, in verbose mode (shows files as they are copied):

`cp -vr {{path/to/source_directory}} {{path/to/target_directory}}`

- Copy text files to another location, in interactive mode (prompts user before overwriting):

`cp -i {{*.txt}} {{path/to/target_directory}}`

- Dereference symbolic links before copying:

`cp -L {{link}} {{path/to/target_directory}}`

- Use the full path of source files, creating any missing intermediate directories when copying:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
