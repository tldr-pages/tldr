# update-initramfs

> Manage initramfs.
> More information: <https://manned.org/update-initramfs>.

- Create a new initramfs (use `all` for all installed kernel versions):

`sudo update-initramfs -c -k {{kernel_version}}`

- Update an existing initramfs:

`sudo update-initramfs -u`

- Remove an existing initramfs (be careful when using `all` for `kernel_version`):

`sudo update-initramfs -d -k {{kernel_version}}`
