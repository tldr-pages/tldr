# update-initramfs

> Manage initramfs.
> More information: <https://manned.org/update-initramfs>.

- Create a new initramfs:

`sudo update-initramfs -c -k {{kernel_version}}`

- Update an existing initramfs:

`initramfs -u`

- Remove an existing initramfs:

`initramfs -d`
