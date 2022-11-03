# czkawka-cli

> Multi functional app to find duplicates, empty folders, similar images etc. Command-line version.
> More information: <https://github.com/qarmin/czkawka>.

- Find [dup]licate files in directory:

`czkawka-cli dup --directories {{path/to/directory}}`

- Find [dup]licate files and delete them (default: `NONE`):

`czkawka-cli dup --directories {{path/to/directory}} --delete-method {{AEN/AEO/ON/OO/HARD/NONE}}`

- Find similar [image]s:

`czkawka-cli image --directories {{path/to/directory}}`
