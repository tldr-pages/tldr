# exif

> Show and change EXIF information in JPEG files.
> More information: <https://manned.org/exif>.

- Show all recognized EXIF information in an image:

`exif {{path/to/image.jpg}}`

- Show a table listing known EXIF tags and whether each one exists in an image:

`exif {{[-l|--list-tags]}} --no-fixup {{path/to/image.jpg}}`

- Extract the image thumbnail into a separate file:

`exif {{[-e|--extract-thumbnail]}} {{[-o|--output]}} {{path/to/thumbnail.jpg}} {{path/to/image.jpg}}`

- Show the raw contents of the "Model" tag in the given image:

`exif --ifd {{0}} {{[-t|--tag]}} "Model" {{[-m|--machine-readable]}} {{path/to/image.jpg}}`

- Change the value of the "Artist" tag to John Smith and save to `new.jpg`:

`exif {{[-o|--output]}} {{path/to/new.jpg}} --ifd {{0}} {{[-t|--tag]}} "Artist" --set-value "John Smith" --no-fixup {{path/to/image.jpg}}`
