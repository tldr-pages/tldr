# grub-editenv

> Edit GRUB environment variables.
> More information: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- Set a default boot entry (Assuming the boot entry already exists):

`grub-editenv /boot/grub/grubenv set default={{Ubuntu}}`

- Display the current value of the `timeout` variable:

`grub-editenv /boot/grub/grubenv list timeout`

- Reset the `saved_entry` variable to the default:

`grub-editenv /boot/grub/grubenv unset saved_entry`

- Append "quiet splash" to the kernel command line:

`grub-editenv /boot/grub/grubenv list kernel_cmdline`
