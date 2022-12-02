# diff

> Compare files and directories.
> More information: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Compare files (lists changes to turn `old_file` into `new_file`):

`diff {{path/to/file}} {{path/to/file}}`

- Compare files, ignoring white spaces:

`diff --ignore-all-space {{path/to/file}} {{path/to/file}}`

- Compare files, showing the differences side by side:

`diff --side-by-side {{path/to/file}} {{path/to/file}}`

- Compare files, showing the differences in unified format (as used by `git diff`):

`diff --unified {{path/to/file}} {{path/to/file}}`

- Compare directories recursively (shows names for differing files/directories as well as changes made to files):

`diff --recursive {{old_directory}} {{new_directory}}`

- Compare directories, only showing the names of files that differ:

`diff --recursive --brief {{old_directory}} {{new_directory}}`

- Create a patch file for Git from the differences of two text files, treating nonexistent files as empty:

`diff --text --unified --new-file {{path/to/file}} {{path/to/file}} > {{diff.patch}}`
