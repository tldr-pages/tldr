# grub-bios-setup

> Set up a device to use GRUB with a BIOS configuration.
> You should use `grub-install` instead of `grub-bios-setup` in most cases.
> More information: <https://manned.org/grub-bios-setup.8>.

- Set up a device to boot with GRUB:

`grub-bios-setup {{/dev/sdX}}`

- Install even if problems are detected:

`grub-bios-setup --force {{/dev/sdX}}`

- Install GRUB in a specific directory:

`grub-bios-setup --directory={{/boot/grub}} {{/dev/sdX}}`
