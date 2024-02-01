# split

> Split a file into pieces.
> More information: <https://keith.github.io/xcode-man-pages/split.1.html>.

- Split a file, each split having 10 lines (except the last split):

`split -l {{10}} {{filename}}`

- Split a file by a regular expression. The matching line will be the first line of the next output file:

`split -p {{cat|^[dh]og}} {{filename}}`

- Split a file with 512 bytes in each split (except the last split; use 512k for kilobytes and 512m for megabytes):

`split -b {{512}} {{filename}}`

- Split a file into 5 files. File is split such that each split has same size (except the last split):

`split -n {{5}} {{filename}}`
