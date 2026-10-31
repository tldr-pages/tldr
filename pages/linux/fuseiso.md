# fuseiso

> FUSE module to mount ISO, BIN, NRG, MDF and IMG filesystem images.
> More information: <https://manned.org/fuseiso>.

- Mount an ISO image to a given directory:

`fuseiso {{path/to/image.iso}} {{path/to/mount_point}}`

- Mount an ISO image, automatically creating the mount point if it doesn't exist (and deleting it on unmount):

`fuseiso -p {{path/to/image.iso}} {{path/to/mount_point}}`

- Mount an ISO image in the foreground (useful for debugging):

`fuseiso -f {{path/to/image.iso}} {{path/to/mount_point}}`

- Unmount an image using the standard FUSE unmount utility:

`fusermount3 -u {{path/to/mount_point}}`
