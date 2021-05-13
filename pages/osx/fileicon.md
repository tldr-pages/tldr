# fileicon

> a macOS CLI for managing custom icons for files and folders, as a programmatic alternative to interactively using Finder.
> More information: <https://github.com/mklement0/fileicon>.

- Assign custom icon derived from image file 'img.png' to file 'foo':

`fileicon set foo img.png`

- Remove previously assigned custom icon from folder 'foodir':

`fileicon rm foodir`

- Extract custom icon from file 'foo' to icon file 'foo.icns':

`fileicon get foo`

- Test if folder 'foodir' has custom icon:

`fileicon test foodir`
