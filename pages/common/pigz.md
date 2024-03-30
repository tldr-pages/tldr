# pigz

> Multithreaded zlib compression utility.
> More information: <https://github.com/madler/pigz>.

- Compress a file with default options:

`pigz {{path/to/file}}`

- Compress a file using the best compression method:

`pigz -9 {{path/to/file}}`

- Compress a file using no compression and 4 processors:

`pigz -0 -p{{4}} {{path/to/file}}`

- Compress a directory using tar:

`tar cf - {{path/to/directory}} | pigz > {{path/to/file.tar.gz}}`

- Decompress a file:

`pigz -d {{archive.gz}}`

- List the contents of an archive:

`pigz -l {{archive.tar.gz}}`
