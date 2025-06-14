# tar

> archive files using tar (tape archives)
> often combined with compression utilities like gzip

- create a `.tar` archive:
`tar -cvf archive.tar file1 file2`

- extract a `.tar` archive
`tar -xvf archive.tar`

- create a gzip compressed archive:
`tar -czvf archive.tar.gz file 1file2`

- extract a gzip compressed archive:
`tar -xzvf archive.tar.gz`

- list contents of an archive:
`tar -tvf archive.tar`
