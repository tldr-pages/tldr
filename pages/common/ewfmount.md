# ewfmount

> Mount data stored in Expert Witness Compression Format (EWF) files.
> More information: <https://manpages.debian.org/unstable/ewf-tools/ewfmount.1.en.html>.

- Mount an EWF image file:

`ewfmount {{path/to/image.E01}} {{path/to/mount_point}}`

- Mount an EWF image using the raw input format:

`ewfmount -f raw {{path/to/image.E01}} {{path/to/mount_point}}`

- Mount logical volume files only:

`ewfmount -f files {{path/to/image.E01}} {{path/to/mount_point}}`

- Mount an EWF image with verbose output:

`ewfmount -v {{path/to/image.E01}} {{path/to/mount_point}}`
