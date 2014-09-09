# tar

> Archiving utility
> Optional compression with gzip / bzip

- create an archive from files

`tar cf {{target.tar}} {{file1 file2 file3}}`

- create a gzipped archive

`tar czf {{target.tar.gz}} {{file1 file2 file3}}`

- extract an archive in a target folder

`tar xf {{source.tar}} -C {{folder}}`

- extract a gzipped archive in the current directory

`tar xzf {{source.tar.gz}}`

- extract a bzipped archive in the current directory

`tar xjf {{source.tar.bz2}}`

- create a compressed archive, using archive suffix to determine the compression programm

`tar caf {{target.tar.xz}} {{file1 file2 file3}}`

- list the contents of a tar file

`tar -tvf {{source.tar}}`
