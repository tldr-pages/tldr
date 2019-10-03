# sdiff

> Compare the differences and/or merge between two files.

- Compare 2 files:

`sdiff {{path/to/first_file}} {{path/to/second_file}}`

- Compare 2 files, ignoring all tabs and whitespace:

`sdiff -W {{path/to/first_file}} {{path/to/second_file}}`

- Compare between two files, ignore white space at the end of the line:

`sdiff -Z {{path/to/first_file}} {{path/to/second_file}}`

- Compare between two files, case insensitive:

`sdiff -i {{path/to/first_file}} {{path/to/second_file}}`

- Compare between two files then merge and create new file:

`sdiff -o {{path/to/new_merge_file}} {{path/to/first_file}} {{path/to/second_file}}`
