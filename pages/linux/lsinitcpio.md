# lsinitcpio

> View the contents of an initramfs image.
> See also: `mkinitcpio`.
> More information: <https://manned.org/lsinitcpio>.

- View a list of all files and directories in the image:

`lsinitcpio {{path/to/initramfs.img}}`

- Extract the image to the current directory:

`lsinitcpio --extract {{path/to/initramfs.img}}`

- View human-readable information on the image:

`lsinitcpio --analyze {{path/to/initramfs.img}}`
