# split

> Split a file into pieces.

- Split a file, each split having 10 lines (except the last split):

`split -l 10 {{filename}}`

- Split a file into 5 files. File is split such that each split has same size (except the last split):

`split -n 5 {{filename}}`

- Split a file with at most 512 bytes of lines in each split:

`split -C 512 {{filename}}`
