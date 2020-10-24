# sxiv

> Simple X Image Viewer.
> More information: <https://github.com/muennich/sxiv>.

- Open an image:

`sxiv {{path/to/file}}`

- Open an image in fullscreen mode:

`sxiv -f {{path/to/file}}`

- Open a newline-separated list of images, reading filenames from standard input:

`echo {{path/to/file}} | sxiv -i`

- Open a space-separated list of images as a slideshow:

`sxiv -S {{seconds}} {{path/to/file}}`

- Open a space-separated list of images in thumbnail mode:

`sxiv -t {{path/to/file}}`
