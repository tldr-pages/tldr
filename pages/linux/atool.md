# atool

> Manage archives of various formats.
> More information: <https://www.nongnu.org/atool/>.

- List files in a zip archive:

`atool --list {{foo.zip}}`

- Unpack a tar.gz archive into a new subdirectory (or current directory if it contains only one file):

`atool --extract {{bar.tar.gz}}`

- Create a new 7zip archive:

`atool --add {{archive.7z}} {{foo}} {{bar}}`

- Extract all zip and rar archives in the current directory:

`atool --each --extract *.zip *.rar`
