# xmount

> xmount allows you to convert on-the-fly between multiple input and output harddisk image types with optional write cache support.
> xmount creates a virtual file system using FUSE (Filesystem in Userspace) that contains a virtual representation of the input image.
> 
> More information: <https://www.pinguin.lu/xmount>.


- Mounting an RAW-Imagefile into a DMG-container file:

`xmount --in raw IMAGE.dd --out dmg MOUNTPOINT`

- Mounting an EWF-Imagefile with write-cache support into a VHD file to boot from:

`xmount --cache CACHE.ovl --in ewf IMAGE.E?? --out vhd MOUNTPOINT`

- Mounting first partition at sector 2048 into a new RAW-Image:

`xmount --offset 2048 --in raw IMAGE.dd --out  raw MOUNTPOINT`
