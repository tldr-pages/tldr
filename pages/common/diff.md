# diff

> Compare files and directories.
> More information: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Compare files (lists changes to turn `old_file` into `new_file`):

`diff {{old_file}} {{new_file}}`

- Compare files, ignoring white spaces:

`diff --ignore-all-space {{old_file}} {{new_file}}`

- Compare files, showing the differences side by side:

`diff --side-by-side {{old_file}} {{new_file}}`

- Compare files, showing the differences in unified format (as used by `git diff`):

`diff --unified {{old_file}} {{new_file}}`

- Compare directories recursively (shows names for differing files/directories as well as changes made to files):

`diff --recursive {{old_directory}} {{new_directory}}`

- Compare directories, only showing the names of files that differ:

`diff --recursive --brief {{old_directory}} {{new_directory}}`

- Create patch file from the differences of two directories or files:

`diff --text --unified --new-file {{old_file_or_directory}} {{new_file_or_directory}} > {{diff.patch}}`
