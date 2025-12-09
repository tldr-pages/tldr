# mkfs.erofs

> Create an EROFS filesystem in an image.
> More information: <https://manned.org/mkfs.erofs>.

- Create an EROFS filesystem based on the root directory:

`mkfs.erofs image.erofs root/`

- Create an EROFS image with a specific UUID:

`mkfs.erofs -U {{UUID}} image.erofs root/`

- Create a compressed EROFS image:

`mkfs.erofs -zlz4hc image.erofs root/`

- Create an EROFS image where all files are owned by root:

`mkfs.erofs --all-root image.erofs root/`
