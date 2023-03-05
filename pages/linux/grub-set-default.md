# grub-set-default

> Set the default boot entry for GRUB.
> More information: <https://manned.org/grub-set-default>.

- Set the default boot entry to an entry number, name or identifier:

`sudo grub-set-default {{entry_number}}`

- Set the default boot entry to an entry number, name or identifier for an alternative boot directory:

`sudo grub-set-default --boot-directory {{/path/to/boot_directory}} {{entry_number}}`
