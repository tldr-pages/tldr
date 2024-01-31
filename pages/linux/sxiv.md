# sxiv

> Simple X Image Viewer.
> More information: <https://github.com/muennich/sxiv>.

- Open an image:

`sxiv {{path/to/image}}`

- Open an image in fullscreen mode:

`sxiv -f {{path/to/file}}`

- Open a newline-separated list of images, reading filenames from `stdin`:

`echo {{path/to/file}} | sxiv -i`

- Open one or more images as a slideshow:

`sxiv -S {{seconds}} {{path/to/image1 path/to/image2}}`

- Open one or more images in thumbnail mode:

`sxiv -t {{path/to/image1 path/to/image2}}`
