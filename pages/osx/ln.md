#ln

> Creates a link between files
> Can create either a hard link to the filesystem or a symbolic link to a filename
> Can create links to a file or to a directory

- Create hard ling to target in current directory

`ln {{target}}`

- Create symlink to target in current directory

`ln -s {{target}}`

- Create a symlink with the specified name in current directory

`ln -s {{target}} {{link_name}}`

- Create symlink to target in different directory. Omit -s flag for hard link

`ln -s -t {{full_path_to_directory}} {{target}}`
