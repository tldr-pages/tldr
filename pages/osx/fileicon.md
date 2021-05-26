# fileicon

> A macOS CLI to manage custom file and folder icons.
> More information: <https://github.com/mklement0/fileicon>.

- Set a custom icon for a specific file or directory:

`fileicon set {{path/to/file_or_directory}} {{path/to/icon.png}}`

- Remove a custom icon from a specific file or directory:

`fileicon rm {{path/to/file_or_directory}}`

- Extract custom icon from file 'foo' to icon file 'foo.icns':

`fileicon get foo`

- Test if a specific file or directory has a custom icon:

`fileicon test {{path/to/file_or_directory}}`
