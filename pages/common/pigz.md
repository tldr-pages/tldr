# pigz

> Multithreaded zlib compression utility.
> More information: <https://github.com/madler/pigz>.

- Compress a file with default options:

`pigz {{filename}}`

- Compress a file using the best compression method:

`pigz -9 {{filename}}`

- Compress a file using no compression and 4 processors:

`pigz -0 -p{{4}} {{filename}}`

- Decompress a file:

`pigz -d {{archive.gz}}`

- List the contents of an archive:

`pigz -l {{archive.tar.gz}}`
