# split

> Split a file into pieces

- Split a file with 10 lines in each split (except last split)

`split -l 10 {{filename}}`

- Split a file into 5 files. All the splits have same size (not necessarily same number of lines)

`split -n 5 {{filename}}`

- Split a file with 512 bytes of lines in each split (most useful)

`split -C 512 {{filename}}`

