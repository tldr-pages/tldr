# mkfile

> Create empty files of any size.
> More information: <https://manned.org/mkfile>.

- Create an empty file of 15 kilobytes:

`mkfile -n {{15k}} {{path/to/file}}`

- Create a file of a given size and unit (bytes, KB, MB, GB):

`mkfile -n {{size}}{{b|k|m|g}} {{path/to/file}}`

- Create two files of 4 megabytes each:

`mkfile -n {{4m}} {{first_filename}} {{second_filename}}`
