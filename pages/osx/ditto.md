# ditto

> Copy files and directories, and create or extract archives.
> More information: <https://keith.github.io/xcode-man-pages/ditto.1.html>.

- Merge a source directory into a destination directory, overwriting files with the same names:

`ditto {{path/to/source_directory}} {{path/to/destination_directory}}`

- Print a line to the Terminal window for every file that's being copied:

`ditto -V {{path/to/source_directory}} {{path/to/destination_directory}}`

- Copy a file or directory, explicitly preserving resource forks and HFS metadata:

`ditto --rsrc {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}}`

- Create a ZIP archive containing the source directory and preserving resource forks and HFS metadata:

`ditto -c -k --sequesterRsrc --keepParent {{path/to/source_directory}} {{path/to/archive.zip}}`

- Extract a ZIP archive into a directory:

`ditto -x -k {{path/to/archive.zip}} {{path/to/destination_directory}}`
