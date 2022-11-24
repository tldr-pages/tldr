# setfile

> Sets file attributes on files in an HFS+ directory.
> More information: <https://ss64.com/osx/setfile.html>.

- Set creation date for file:

`setfile -d "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file}}`

- Set modification date for file:

`setfile -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file}}`

- Set modification date for symlink file (not to linked file itself):

`setfile -P -m "{{MM/DD/YYYY HH:MM:SS}}" {{path/to/file}}`
