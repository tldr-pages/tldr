# grub-mkimage

> Make a bootable GRUB image.
> More information: <https://man.archlinux.org/man/grub-mkimage.1>.

- Create a GRUB image for a UEFI system, including specific modules:

`grub-mkimage {{[-O|--format]}} {{x86_64-efi}} {{[-p|--prefix]}} {{/boot/grub}} {{[-o|--output]}} {{path/to/grub.efi}} {{part_gpt ext2}}`

- Create a core image for a BIOS system, including the specified modules:

`grub-mkimage {{[-O|--format]}} {{i386-pc}} {{[-p|--prefix]}} {{/boot/grub}} {{[-o|--output]}} {{path/to/core.img}} {{biosdisk part_msdos ext2}}`

- Embed a configuration file in the image:

`grub-mkimage {{[-O|--format]}} {{x86_64-efi}} {{[-p|--prefix]}} {{/boot/grub}} {{[-c|--config]}} {{path/to/embedded.cfg}} {{[-o|--output]}} {{path/to/grub.efi}} {{part_gpt ext2}}`

- Use GRUB images and modules from a specific directory:

`grub-mkimage {{[-d|--directory]}} {{/usr/lib/grub/x86_64-efi}} {{[-O|--format]}} {{x86_64-efi}} {{[-p|--prefix]}} {{/boot/grub}} {{[-o|--output]}} {{path/to/grub.efi}} {{part_gpt ext2}}`

- Print verbose messages while creating the image:

`grub-mkimage {{[-v|--verbose]}} {{[-O|--format]}} {{x86_64-efi}} {{[-p|--prefix]}} {{/boot/grub}} {{[-o|--output]}} {{path/to/grub.efi}} {{part_gpt ext2}}`

- Display help:

`grub-mkimage {{[-?|--help]}}`

- Display version:

`grub-mkimage {{[-V|--version]}}`
