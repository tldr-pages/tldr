# grub-mount

> Mount a filesystem or filesystem image read-only using GRUB's filesystem drivers.
> More information: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmount>.

- Mount a block device or filesystem image to a mount point:

`grub-mount {{/dev/sdXY}} {{/mnt}}`

- Mount an entire disk image's second partition, `-r` specifies the partition number in the image:

`grub-mount {{[-r|--root]}} {{2}} {{disk.img}} {{/mnt}}`

- Mount an encrypted device and prompt for a passphrase:

`grub-mount {{[-C|--crypto]}} {{/dev/sdXY}} {{/mnt}}`

- Load a ZFS encryption key from a file:

`grub-mount {{[-K|--zfs-key]}} /{{path/to/zfs.key}} {{/dev/sdX}} {{/mnt}}`

- Show debugging output for a matching category:

`grub-mount {{[-d|--debug]}} {{string}} {{image}} {{/mnt}}`

- Enable verbose output:

`grub-mount {{[-v|--verbose]}} {{image}} {{/mnt}}`

- Display help:

`grub-mount {{[-?|--help]}}`

- Display version:

`grub-mount --version`
