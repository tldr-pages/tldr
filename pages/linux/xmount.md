# xmount

> Convert on-the-fly between multiple input and output hard disk image types with optional write cache support.
> Creates a virtual file system using FUSE (Filesystem in Userspace) that contains a virtual representation of the input image.
> More information: <https://manned.org/xmount>.

- Mount a `.raw` image file into a DMG container file:

`xmount --in {{raw}} {{path/to/image.dd}} --out {{dmg}} {{mountpoint}}`

- Mount an EWF image file with write-cache support into a VHD file to boot from:

`xmount --cache {{path/to/cache.ovl}} --in {{ewf}} {{path/to/image.E??}} --out {{vhd}} {{mountpoint}}`

- Mount the first partition at sector 2048 into a new `.raw` image file:

`xmount --offset {{2048}} --in {{raw}} {{path/to/image.dd}} --out {{raw}} {{mountpoint}}`
