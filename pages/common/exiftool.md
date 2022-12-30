# exiftool

> Read and write meta information in files.
> More information: <https://exiftool.org>.

- Print the EXIF metadata for a given file:

`exiftool {{path/to/file}}`

- Remove all EXIF metadata from the given files:

`exiftool -All= {{path/to/file1 path/to/file2 ...}}`

- Remove GPS EXIF metadata from given image files:

`exiftool "-gps*=" {{path/to/image1 path/to/image2 ...}}`

- Remove all EXIF metadata from the given image files, then re-add metadata for color and orientation:

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation {{image1 image2 ...}}`

- Move the date at which all photos in a directory were taken 1 hour forward:

`exiftool "-AllDates+=0:0:0 1:0:0" {{path/to/directory}}`

- Move the date at which all JPEG photos in the current directory were taken 1 day and 2 hours backward:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Only change the `DateTimeOriginal` field subtracting 1.5 hours, without keeping backups:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Recursively rename all JPEG photos in a directory based on the `DateTimeOriginal` field:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e {{path/to/directory}} -r -ext jpg`
