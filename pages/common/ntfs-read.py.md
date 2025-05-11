# ntfs-read.py

> A read-only NTFS explorer for accessing and extracting files from NTFS volumes.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Open an NTFS volume for exploration (e.g., `C:\.\\` or `/dev/disk1s1`):

`ntfs-read.py {{volume}}`

- Extract a specific file from an NTFS volume (e.g., `\windows\system32\config\sam`):

`ntfs-read.py -extract {{\windows\system32\config\sam}} {{volume}}`

- Enable debug output:

`ntfs-read.py -debug {{volume}}`

- Display help:

`ntfs-read.py --help`
