# cpio

> Copies files to and from archives.

- Take a list of file names from standard input and creates an archive from them:

`echo "{{file1}} {{file2}} {{file3}}" | cpio -o > {{[o]utput_archive.cpio}}`

- Create an archive containing all the files and folders in a directory in [v]erbose mode:

`find {{path/to/directory}} | cpio -ov > {{[o]utput_archive.cpio}}`

- Extract files from an archive, generating [d]irectories where needed, in [v]erbose mode:

`cpio -idv < {{[i]nput_archive.cpio}}`
