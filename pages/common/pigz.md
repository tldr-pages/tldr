# pigz

> Multithreaded zlib compression utility.

- Compress a file with default options:

`pigz {{filename.ext}}`

- Compress a file using compression method [1-9] and number of processors [-pN]:

`pigz -9 -p8 {{filename.ext}}`

- Decompress a file:

`pigz -d {{archive.gz}}`

- List the contents of an archive:

`pigz -l {{archive.tar.gz}}`

- Create an compressed archive when piped with tar:

`tar cvf - {{directory/to/archive}} | pigz -9 -p8 > {{archive.tar.gz}}`