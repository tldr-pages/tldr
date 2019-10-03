# sdiff

> Compare the differences and/or merge between two files.

- Compare 2 files:

`sdiff {{path/to/first_file}} {{path/to/second_file}}`

- Compare 2 files, ignoring all tabs and whitespace:

`sdiff -W {{path/to/first_file}} {{path/to/second_file}}`

- Compare 2 files, ignoring whitespace at the end of lines:

`sdiff -Z {{path/to/first_file}} {{path/to/second_file}}`

- Case insensitively compare 2 files:

`sdiff -i {{path/to/first_file}} {{path/to/second_file}}`

- Compare 2 files and then merge, creating a new file:

`sdiff -o {{path/to/new_merge_file}} {{path/to/first_file}} {{path/to/second_file}}`
