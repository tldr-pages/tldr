# cpio

> Archiving utility.

- Create an archive from files

`echo "{{file1}} {{file2}} {{file3}}" | cpio -ov > {{archive.cpio}}`

- Create an archive from a directory

`find {{directory}} | cpio -ov > {{archive.cpio}}`

- Extract an archive

`cpio -idv < {{archive.cpio}}`

