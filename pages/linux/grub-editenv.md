# grub-editenv

> Edit GRUB environment variables on Linux.

- Set the default boot entry to "Ubuntu" (Assuming the boot entry exists):

  `grub-editenv /boot/grub/grubenv set default=Ubuntu`

- Display the current value of the `timeout` variable:

  `grub-editenv /boot/grub/grubenv list timeout`

- Reset the `saved_entry` variable to the default:

  `grub-editenv /boot/grub/grubenv unset saved_entry`

- Append "quiet splash" to the kernel command line:

  `grub-editenv /boot/grub/grubenv list kernel_cmdline`
