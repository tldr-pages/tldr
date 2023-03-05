# grub-reboot

> Set the default boot entry for GRUB, for the next boot only.
> More information: <https://manned.org/grub-reboot>.

- Set the default boot entry to an entry number, name or identifier for the next boot:

`sudo grub-reboot {{entry_number}}`

- Set the default boot entry to an entry number, name or identifier for an alternative boot directory for the next boot:

`sudo grub-reboot --boot-directory {{/path/to/boot_directory}} {{entry_number}}`
