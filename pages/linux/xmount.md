# xmount

> Convert on-the-fly between multiple input and output harddisk image types with optional write cache support.
> Creates a virtual file system using FUSE (Filesystem in Userspace) that contains a virtual representation of the input image.
> More information: <https://www.pinguin.lu/xmount>.

- Mount a RAW image file into a DMG container file:

`xmount --in {{raw}} {{path/to/image.dd}} --out {{dmg}} {{mountpoint}}`

- Mount an EWF-Imagefile with write-cache support into a VHD file to boot from:

`xmount --cache CACHE.ovl --in ewf IMAGE.E?? --out vhd MOUNTPOINT`

- Mount first partition at sector 2048 into a new RAW image file:

`xmount --offset {{2048}} --in {{raw}} {{path/to/image.dd}} --out {{raw}} {{mountpoint}}`
