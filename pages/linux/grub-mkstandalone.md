# grub-mkstandalone

> Make a standalone GRUB image with a configuration file embedded in a memory disk.
> More information: <https://man.archlinux.org/man/grub-mkstandalone.1>.

- Create a standalone GRUB image for a UEFI system, embedding a configuration file:

`grub-mkstandalone --format {{x86_64-efi}} --output {{path/to/grub.efi}} "boot/grub/grub.cfg={{path/to/grub.cfg}}"`

- Pre-load specific modules:

`grub-mkstandalone --format {{x86_64-efi}} --modules "{{part_gpt ext2}}" --output {{path/to/grub.efi}} "boot/grub/grub.cfg={{path/to/grub.cfg}}"`

- Set the compression type used for the core image:

`grub-mkstandalone --format {{x86_64-efi}} --core-compress {{xz|none|auto}} --output {{path/to/grub.efi}} "boot/grub/grub.cfg={{path/to/grub.cfg}}"`

- Print verbose messages while creating the image:

`grub-mkstandalone --verbose --format {{x86_64-efi}} --output {{path/to/grub.efi}} "boot/grub/grub.cfg={{path/to/grub.cfg}}"`

- Display help:

`grub-mkstandalone {{[-?|--help]}}`

- Display version:

`grub-mkstandalone --version`
