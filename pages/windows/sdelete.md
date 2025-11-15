# sdelete

> Securely delete file/directory from disk, or clean the free space on a volume/physical disk.
> More information: <https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>.

- Delete files with 3 [p]asses:

`sdelete -p 3 {{path\to\file1 path\to\file2 ...}}`

- Delete folders and its [s]ubdirectories with 1 pass (default):

`sdelete -s {{path\to\directory1 path\to\directory2 ...}}`

- Clean the free space of volume D: with 3 [p]asses:

`sdelete -p 3 D:`

- Clean the free space with [z]eros of physical disk 2, which should not contain any volumes to be cleaned:

`sdelete -z 2`
