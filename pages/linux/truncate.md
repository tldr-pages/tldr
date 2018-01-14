# truncate

> Shrink or extend the size of a file to the specified size.

- Set the size of an existing file, or create a new file with the specified size:

`truncate -s 10G {{filename}}`

- Extend the file size, fill with holes (which reads as zero bytes):

`truncate -s +50M {{filename}}`

- Shrink the file and discard the extra data:

`truncate -s -2G {{filename}`
