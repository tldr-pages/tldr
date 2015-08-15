# exiftool

> Read and write meta information in files

- Remove all EXIF metadata from the given files

`exiftool -All= {{file}}`

- Increase time photo taken by 1 hour in directory

`exiftool "-AllDates+=0:0:0 1:0:0" {{directory}}`

- Decrease time photo taken by 1 day and 2 hours on jpg's only

`exiftool "-AllDates-=0:0:1 2:0:0" {{*.jpg}}`
