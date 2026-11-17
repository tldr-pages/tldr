# grub-mkstandalone

> Generate a standalone GRUB image containing all modules (and optionally files like grub.cfg) in a memory disk.
> More information: <https://man.archlinux.org/man/grub-mkstandalone.1>.

- Create a standalone GRUB image for a UEFI system, embedding a configuration file:

`grub-mkstandalone {{[-O|--format]}} {{x86_64-efi}} {{[-o|--output]}} {{path/to/grub.efi}} "boot/grub/grub.cfg={{path/to/grub.cfg}}"`

- Pre-load specific modules:

`grub-mkstandalone {{[-O|--format]}} {{x86_64-efi}} --modules "{{part_gpt ext2}}" --output {{path/to/grub.efi}} "boot/grub/grub.cfg={{path/to/grub.cfg}}"`

- Print verbose messages while creating the image:

`grub-mkstandalone {{[-v|--verbose]}} {{[-O|--format]}} {{x86_64-efi}} {{[-o|--output]}} {{path/to/grub.efi}} "boot/grub/grub.cfg={{path/to/grub.cfg}}"`

- Display help:

`grub-mkstandalone {{[-?|--help]}}`

- Display version:

`grub-mkstandalone {{[-V|--version]}}`
