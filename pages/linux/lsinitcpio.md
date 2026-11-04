# lsinitcpio

> View the contents of an initramfs image.
> See also: `mkinitcpio`.
> More information: <https://manned.org/lsinitcpio>.

- View a list of all files and directories of a specific image:

`lsinitcpio {{path/to/initramfs.img}}`

- Extract an image to the current directory:

`lsinitcpio {{[-x|--extract]}} {{path/to/initramfs.img}}`

- View human-readable information on an image:

`lsinitcpio {{[-a|--analyze]}} {{path/to/initramfs.img}}`
