# exiftool

> Read and write meta information in files.
> More information: <https://owl.phy.queensu.ca/~phil/exiftool>.

- Remove all EXIF metadata from the given files:

`exiftool -All= {{file}}`

- Increase time photo taken by 1 hour in directory:

`exiftool "-AllDates+=0:0:0 1:0:0" {{directory}}`

- Decrease time photo taken by 1 day and 2 hours on JPEGs only:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Change only DateTimeOriginal by -1.5 hours & do not keep backups:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Rename all JPEGs according to a DateTimeOriginal recursively:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e {{directory}} -r -ext jpg`
