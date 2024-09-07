# setfile

> Set file attributes on files in an HFS+ directory.
> More information: <https://ss64.com/osx/setfile.html>.

- Set creation date for specific files:

`setfile -d "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`

- Set modification date for specific files:

`setfile -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`

- Set modification date for symlink file (not to linked file itself):

`setfile -P -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file1 path/to/file2 ...}}`
