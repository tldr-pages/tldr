# cpio

> Copies files in and out of archives.
> Supports following archive formats: binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar, and POSIX.1 tar.

- Take a list of file names from standard input and copy them [o]ut to an archive in binary format:

`echo "{{file1}} {{file2}} {{file3}}" | cpio -o > {{archive.cpio}}`

- Copy [o]ut all files and folders in a directory to an archive, in [v]erbose mode:

`find {{path/to/directory}} | cpio -ov > {{archive.cpio}}`

- Copy [i]n all files from an archive, generating [d]irectories where needed, in [v]erbose mode:

`cpio -idv < {{archive.cpio}}`
