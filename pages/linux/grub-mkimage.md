# grub-mkimage

> Make a bootable GRUB image.
> More information: <https://man.archlinux.org/man/grub-mkimage.1>.

- Create a GRUB image for a UEFI system, including specific modules:

`grub-mkimage --format {{x86_64-efi}} --prefix {{/boot/grub}} --output {{path/to/grub.efi}} {{part_gpt ext2}}`

- Create a core image for a BIOS system:

`grub-mkimage --format {{i386-pc}} --prefix {{/boot/grub}} --output {{path/to/core.img}} {{biosdisk part_msdos ext2}}`

- Embed a configuration file in the image:

`grub-mkimage --format {{x86_64-efi}} --prefix {{/boot/grub}} --config {{path/to/embedded.cfg}} --output {{path/to/grub.efi}} {{part_gpt ext2}}`

- Set the compression type used for the image:

`grub-mkimage --format {{x86_64-efi}} --prefix {{/boot/grub}} --compression {{xz|none|auto}} --output {{path/to/grub.efi}} {{part_gpt ext2}}`

- Print verbose messages while creating the image:

`grub-mkimage --verbose --format {{x86_64-efi}} --prefix {{/boot/grub}} --output {{path/to/grub.efi}} {{part_gpt ext2}}`

- Display help:

`grub-mkimage {{[-?|--help]}}`

- Display version:

`grub-mkimage --version`
