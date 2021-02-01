# genfstab

> Generate output suitable for addition to an fstab file.
> More information: <https://man.archlinux.org/man/extra/arch-install-scripts/genfstab.8.en>.

- Generate the output based on LABEL:

`genfstab -L MOUNTPOINT`

- Generate the output based on UUID:

`genfstab -U MOUNTPOINT`

- Generate a fstab file, requires being a superuser:

`genfstab -U /mnt >> /mnt/etc/fstab`

- Append a filesystem into fstab file to mount it automatically:

`gengstab -U MOUNTPOINT | sudo tee -a /etc/fstab`
