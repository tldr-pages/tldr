# pngcheck

> Forensics tool for validating the integrity of PNG based (`.png`, `.jng`, `.mng`) image files.
> Can also extract embedded images and text from a file.
> More information: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Verify the integrity of an image file:

`pngcheck {{path/to/file.png}}`

- Check the file with [v]erbose and [c]olorized output:

`pngcheck -vc {{path/to/file.png}}`

- Display contents of [t]ext chunks and [s]earch for PNGs within a specific file:

`pngcheck -ts {{path/to/file.png}}`

- Search for, and e[x]tract embedded PNGs within a specific file:

`pngcheck -x {{path/to/file.png}}`
