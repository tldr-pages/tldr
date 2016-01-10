# diff

> Compare files and directories.

- Compare files:

`diff {{file1}} {{file2}}`

- Compare files, ignoring white spaces:

`diff -w {{file1}} {{file2}}`

- Compare files, showing differences side by side:

`diff -y {{file1}} {{file2}}`

- Compare directories recursively:

`diff -r {{directory1}} {{directory2}}`

- Compare directories, only showing the names of files that differ:

`diff -rq {{directory1}} {{directory2}}`
