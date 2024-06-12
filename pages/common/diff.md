# diff

> Compare files and directories.
> More information: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Compare files (lists changes to turn `old_file` into `new_file`):

`diff {{old_file}} {{new_file}}`

- Compare files, ignoring white spaces:

`diff {{-w|--ignore-all-space}} {{old_file}} {{new_file}}`

- Compare files, showing the differences side by side:

`diff {{-y|--side-by-side}} {{old_file}} {{new_file}}`

- Compare files, showing the differences in unified format (as used by `git diff`):

`diff {{-u|--unified}} {{old_file}} {{new_file}}`

- Compare directories recursively (shows names for differing files/directories as well as changes made to files):

`diff {{-r|--recursive}} {{old_directory}} {{new_directory}}`

- Compare directories, only showing the names of files that differ:

`diff {{-r|--recursive}} {{-q|--brief}} {{old_directory}} {{new_directory}}`

- Create a patch file for Git from the differences of two text files, treating nonexistent files as empty:

`diff {{-a|--text}} {{-u|--unified}} {{-N|--new-file}} {{old_file}} {{new_file}} > {{diff.patch}}`

- Compare files, showing output in color and try hard to find smaller set of changes:

`diff {{-d|--minimal}} --color=always {{old_file}} {{new_file}}`
