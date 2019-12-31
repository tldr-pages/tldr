# ect

> Efficient Compression Tool (or ECT) is a C++ file optimizer. It supports PNG, JPEG, GZIP and ZIP files.
> More information: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Compress a file:

`ect {{filename.png}}`

- Compress a file with the highest compression level and multithreading:

`ect -9 --mt-deflate {{filename.png}}`

- Compress all the files in a directory recursively, keeping the original modification time:

`ect -keep -recurse {{directory}}`
