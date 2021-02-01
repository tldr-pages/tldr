# genfstab

> Generate output suitable for addition to an fstab file.
> More information: <https://man.archlinux.org/man/extra/arch-install-scripts/genfstab.8>.

- Generate the output based on LABEL:

`genfstab -L {{path/to/mount_point}}`

- Display `fstab` output using partitions' UUID:

`genfstab -U {{path/to/mount_point}}`

- Generate a fstab file, requires being a superuser:

`genfstab -U {{/mnt}} >> {{/mnt/etc/fstab}}`

- Append a filesystem into fstab file to mount it automatically:

`genfstab -U {{path/to/mount_point}} | sudo tee -a /etc/fstab`
