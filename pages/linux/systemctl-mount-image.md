# systemctl mount-image

> Mount an image file into a unit's mount namespace.
> Only supported for the units that run within a mountspace ie, with `RootImage=`, `PrivateMounts=`, etc.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#%0A%20%20%20%20%20%20%20%20%20%20%20%20mount-image%0A%20%20%20%20%20%20%20%20%20%20%20%20UNIT%0A%20%20%20%20%20%20%20%20%20%20%20%20IMAGE%0A%20%20%20%20%20%20%20%20%20%20%20%20%5BPATH%0A%20%20%20%20%20%20%20%20%20%20%20%20%5BPARTITION_NAME:MOUNT_OPTIONS%5D%5D%0A%20%20%20%20%20%20%20%20%20%20>.

- Mount an image at a specific path inside the unit's mount namespace:

`systemctl mount-image {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}}`

- Mount the image's `root` partition with read-only and no-setuid options:

`systemctl mount-image {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}} root:ro,nosuid`

- Create the destination directory before mounting:

`systemctl mount-image --mkdir {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}}`

- Mount an image as read-only:

`systemctl mount-image --read-only {{unit}} /{{path/to/image}} /{{path/to/directory_inside_unit}}`
