# tar

> Archiving utility
> Optional compression with gzip / bzip

- create an archive from files

`tar cf {{target.tar}} {{file1 file2 file3}}`

- extract an archive in a target folder

`tar xf {{source.tar}} -C {{folder}}`

- create a compressed archive, using archive suffix to determine the compression programm

`tar caf {{target.tar.xz}} {{file1 file2 file3}}`

- compression tool/method (append flag depending on archive type)

`z: use gzip compress`

`j: use bzip2 compress `

`J: use xz compress`

example 1) `tar cfz {{target.tar.gz}} {{file1 file2 file3}}`

example 2) `tar xfj {{source.tar.bz2}}`

- list the contents of a tar file

`tar -tvf {{source.tar}}`
