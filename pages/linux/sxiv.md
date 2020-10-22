# sxiv

> Simple X Image Viewer.
> More information: <https://github.com/muennich/sxiv>.

- View an image:

`sxiv {{path/to/file}}`

- View an image in fullscreen mode:

`sxiv -f {{path/to/file}}`

- View an image or set of images, reading filenames from standard input:

`echo {{path/to/file}} | sxiv -i`

- View images as a slideshow:

`sxiv -S {{delay}} {{path/to/image}} ...`

- View images as thumbnails:

`sxiv -t {{path/to/image}} ...`
