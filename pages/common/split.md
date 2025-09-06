# split

> Split a file into pieces.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>.

- Split a file, each split having 10 lines (except the last split):

`split {{[-l|--lines]}} 10 {{path/to/file}}`

- Split a file into 5 files. File is split such that each split has same size (except the last split):

`split {{[-n|--number]}} 5 {{path/to/file}}`

- Split a file with 512 bytes in each split (except the last split; use 512k for kilobytes and 512m for megabytes):

`split {{[-b|--bytes]}} 512 {{path/to/file}}`

- Split a file with at most 512 bytes in each split without breaking lines:

`split {{[-C|--line-bytes]}} 512 {{path/to/file}}`
