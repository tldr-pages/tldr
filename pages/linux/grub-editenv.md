# grub-editenv

> Edit GRUB environment variables.
> More information: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- Set a default boot entry (Assuming the boot entry already exists):

`grub-editenv /boot/grub/grubenv set default={{Ubuntu}}`

- Display all GRUB environment variables:

`grub-editenv /boot/grub/grubenv list`

- Reset the `saved_entry` variable to the default:

`grub-editenv /boot/grub/grubenv unset saved_entry`
