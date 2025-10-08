# grub-mount

> Mount a file system or file system image read-only using GRUB's file system drivers.
> More information: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmount>.

- Mount a block device or file system image to a mount point:

`grub-mount {{/dev/sda1}} {{/mnt}}`

- Mount an entire disk image's second partition, `-r` specifies the partition number in the image:

`grub-mount -r {{2}} {{disk.img}} {{/mnt}}`

- Mount an encrypted device and prompt for a passphrase:

`grub-mount -C {{/dev/sda2}} {{/mnt}}`

- Load a ZFS encryption key from a file:

`grub-mount -K {{/path/to/zfs.key}} {{/dev/sdX}} {{/mnt}}`

- Show debugging output for a matching category:

`grub-mount -d {{string}} {{image}} {{/mnt}}`

- Enable verbose output:

`grub-mount -v {{image}} {{/mnt}}`

- Show help or version information:

`grub-mount {{[-?|--help]}}`

- Display version information:

`grub-mount --version`
