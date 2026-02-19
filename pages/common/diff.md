# diff

> Compare files and directories.
> See also: `delta`, `difft`.
> More information: <https://manned.org/diff>.

- Compare files (lists changes to turn `old_file` into `new_file`):

`diff {{path/to/old_file}} {{path/to/new_file}}`

- Compare files, ignoring white spaces:

`diff {{[-w|--ignore-all-space]}} {{path/to/old_file}} {{path/to/new_file}}`

- Compare files, showing the differences side by side:

`diff {{[-y|--side-by-side]}} {{path/to/old_file}} {{path/to/new_file}}`

- Compare files, showing the differences in unified format (as used by `git diff`):

`diff {{[-u|--unified]}} {{path/to/old_file}} {{path/to/new_file}}`

- Compare directories recursively (shows names for differing files/directories as well as changes made to files):

`diff {{[-r|--recursive]}} {{path/to/old_directory}} {{path/to/new_directory}}`

- Compare directories, only showing the names of files that differ:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{path/to/old_directory}} {{path/to/new_directory}}`

- Create a patch file for Git from the differences of two text files, treating nonexistent files as empty:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{path/to/old_file}} {{path/to/new_file}} > {{path/to/diff.patch}}`

- Compare files, showing output in color and trying hard to find the smallest set of changes:

`diff {{[-d|--minimal]}} --color=always {{path/to/old_file}} {{path/to/new_file}}`
