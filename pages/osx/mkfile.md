# mkfile

> Create one or more empty files of any size.

- Create an empty file of 15 kilobytes:

`mkfile -n {{15k}} {{filename}}`

- Create a file of a given size and unit (bytes, KB, MB, GB):

`mkfile -n {{size}}{{b|k|m|g}} {{filename}}`

- Create two files of 4 megabytes each:

`mkfile -n {{4m}} {{first_filename}} {{second_filename}}`
