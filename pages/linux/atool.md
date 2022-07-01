# atool

> Manage archives of various formats.
> More information: <https://www.nongnu.org/atool/>.

- List files in a zip archive:

`atool --list {{path/to/archive.zip}}`

- Unpack a tar.gz archive into a new subdirectory (or current directory if it contains only one file):

`atool --extract {{path/to/archive.tar.gz}}`

- Create a new 7zip archive with two files:

`atool --add {{path/to/archive.7z}} {{path/to/file1 path/to/file2 ...}}`

- Extract all zip and rar archives in the current directory:

`atool --each --extract {{*.zip *.rar}}`
