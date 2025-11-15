# jhead

> Image timestamp and EXIF data manipulation.
> More information: <https://www.sentex.net/~mwandel/jhead/usage.html>.

- Show all EXIF data:

`jhead {{path/to/image.jpg}}`

- Set the file's date and time to the EXIF create date (file creation date will be changed):

`jhead -ft {{path/to/image.jpg}}`

- Set the EXIF time to the file's date and time (EXIF data will be changed):

`jhead -dsft {{path/to/image.jpg}}`

- Rename all JPEG files based on the EXIF create date to `YYYY_MM_DD-HH_MM_SS.jpg`:

`jhead -n%Y_%m_%d-%H_%M_%S *.jpg`

- Rotate losslessly all JPEG images by 90, 180 or 270 based on the EXIF orientation tag:

`jhead -autorot *.jpg`

- Update all EXIF timestamps (Format: +- hour:minute:seconds) (example: forgot to change the camera's time zone - removing 1 hour from timestamps):

`jhead -ta-1:00:00 *.jpg`

- Remove all EXIF data (including thumbnails):

`jhead -purejpg {{path/to/image.jpg}}`
