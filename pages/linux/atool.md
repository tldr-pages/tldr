# atool

> Manage archives of various formats.
> More information: <https://manned.org/atool>.

- List files in a Zip archive:

`atool {{[-l|--list]}} {{path/to/archive.zip}}`

- Unpack a tar.gz archive into a new subdirectory (or current directory if it contains only one file):

`atool {{[-x|--extract]}} {{path/to/archive.tar.gz}}`

- Create a new 7z archive with two files:

`atool {{[-a|--add]}} {{path/to/archive.7z}} {{path/to/file1 path/to/file2 ...}}`

- Extract all Zip and rar archives in the current directory:

`atool {{[-e|--each]}} {{[-E|--extract]}} {{*.zip *.rar}}`
