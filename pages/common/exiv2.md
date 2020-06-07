# exiv2

> Image metadata manipulation tool.
> More information: <https://www.exiv2.org/manpage.html>.

- Print a summary of the image Exif metadata:

`exiv2 {{filename}}`

- Print all metadata (Exif, IPTC, XMP) with interpreted values:

`exiv2 -P kt {{filename}}`

- Print all metadata with raw values:

`exiv2 -P kv {{filename}}`

- Delete all metadata from an image:

`exiv2 -d a {{filename}}`

- Delete all metadata, preserving the file timestamp:

`exiv2 -d a -k {{filename}}`

- Rename the file, prepending the date and time from metadata (not from the file timestamp):

`exiv2 -r '%Y%m%d_%H%M%S_:basename:' {{filename}}`
