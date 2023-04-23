# genisoimage

> Pre-mastering program to generate ISO9660/Joliet/HFS hybrid filesystems.
> More information: <https://manpages.debian.org/latest/genisoimage/genisoimage.1.en.html>.

- Create an ISO image from the given source directory:

`genisoimage -o {{myimage.iso}} {{path/to/source_directory}}`

- Create an ISO image with files larger than 2GiB by reporting a smaller apparent size for ISO9660 filesystems:

`genisoimage -o -allow-limited-size {{myimage.iso}} {{path/to/source_directory}}`
