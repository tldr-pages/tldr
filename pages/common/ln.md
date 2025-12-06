# ln

> Create links to files and directories.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- Create a symbolic link to a file or directory:

`ln {{[-s|--symbolic]}} /{{path/to/file_or_directory}} {{path/to/symlink}}`

- Create a symbolic link relative to where the link is located:
- 
`ln {{[-s|--symbolic]}} {{path/to/file_or_directory}} {{path/to/symlink}}`

- Overwrite an existing symbolic link to point to a different file:

`ln {{[-sf|--symbolic --force]}} /{{path/to/new_file}} {{path/to/symlink}}`

- Create a hard link to a file:

`ln /{{path/to/file}} {{path/to/hardlink}}`
