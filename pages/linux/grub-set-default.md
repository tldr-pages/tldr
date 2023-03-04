# grub-set-default

> Set the default boot entry for GRUB.
> More information: <https://manned.org/grub-set-default>.

- Set the boot entry to a entry number, name or identifier:

`sudo grub-set-default {{menu_entry}}`

- Set the boot entry to a entry number, name or identifier for alternative boot directory:

`sudo grub-set-default --boot-directory {{/path/to/directory}} {{menu_entry}}`
