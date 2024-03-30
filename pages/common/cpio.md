# cpio

> Copies files in and out of archives.
> Supports the following archive formats: cpio's custom binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar, and POSIX.1 tar.
> More information: <https://www.gnu.org/software/cpio>.

- Take a list of file names from `stdin` and add them [o]nto an archive in cpio's binary format:

`echo "{{path/to/file1 path/to/file2 ...}}" | cpio -o > {{archive.cpio}}`

- Copy all files and directories in a directory and add them [o]nto an archive, in [v]erbose mode:

`find {{path/to/directory}} | cpio -ov > {{archive.cpio}}`

- P[i]ck all files from an archive, generating [d]irectories where needed, in [v]erbose mode:

`cpio -idv < {{archive.cpio}}`
