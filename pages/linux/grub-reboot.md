# grub-reboot

> Set the default boot entry for GRUB, for the next boot only.
> More information: <https://manned.org/grub-reboot>.

- Set the boot entry to a entry number, name or identifier:

`sudo grub-reboot {{menu_entry}}`

- Set the boot entry to a entry number, name or identifier for alternative boot directory:

`sudo grub-reboot --boot-directory {{/path/to/directory}} {{menu_entry}}`
