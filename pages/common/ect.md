# ect

> Efficient Compression Tool.
> File optimizer written in C++. It supports `.png`, `.jpg`, `.gzip` and `.zip` files.
> More information: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Compress a file:

`ect {{path/to/file.png}}`

- Compress a file with specified compression level and multithreading (1=Fastest (Worst), 9=Slowest (Best), default is 3):

`ect -{{1|2|3|4|5|6|7|8|9}} --mt-deflate {{path/to/file.zip}}`

- Compress all files in a directory recursively:

`ect -recurse {{path/to/directory}}`

- Keep the original modification time:

`ect -keep {{path/to/file.png}}`

- Strip metadata:

`ect -strip {{path/to/file.png}}`
