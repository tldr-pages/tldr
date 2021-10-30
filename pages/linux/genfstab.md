# genfstab

> Arch Linux install script to generate output suitable for addition to an fstab file.
> More information: <https://man.archlinux.org/man/extra/arch-install-scripts/genfstab.8>.

- Display an fstab compatible output based on a volume label:

`genfstab -L {{path/to/mount_point}}`

- Display an fstab compatible output based on a volume UUID:

`genfstab -U {{path/to/mount_point}}`

- A usual way to generate an fstab file, requires root permissions:

`genfstab -U {{/mnt}} >> {{/mnt/etc/fstab}}`

- Append a volume into an fstab file to mount it automatically:

`genfstab -U {{path/to/mount_point}} | sudo tee -a /etc/fstab`
