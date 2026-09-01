# grub-mkimage

> Generate a bootable GRUB image from modules.
> See also: `grub-install`, `grub-mkrescue`.
> More information: <https://manpages.debian.org/unstable/grub2-common/grub-mkimage.1.en.html>.

- Generate an `x86_64` UEFI image with specific modules:

`grub-mkimage {{[-O|--format]}} {{x86_64-efi}} {{[-o|--output]}} {{path/to/grubx64.efi}} {{part_gpt fat normal}}`

- Generate a network boot image with a `(tftp)/grub` prefix:

`grub-mkimage {{[-O|--format]}} {{x86_64-efi}} {{[-o|--output]}} {{path/to/grubx64.efi}} {{[-p|--prefix]}} '(tftp)/grub' {{efinet tftp}}`

- Embed an early configuration file in an image:

`grub-mkimage {{[-O|--format]}} {{x86_64-efi}} {{[-o|--output]}} {{path/to/grubx64.efi}} {{[-c|--config]}} {{path/to/early.cfg}} {{normal}}`

- Use modules from a custom directory:

`grub-mkimage {{[-O|--format]}} {{i386-pc}} {{[-o|--output]}} {{path/to/core.img}} {{[-d|--directory]}} {{path/to/grub_modules}} {{biosdisk part_msdos ext2 normal}}`

- Compress the core image with `xz`:

`grub-mkimage {{[-O|--format]}} {{x86_64-efi}} {{[-o|--output]}} {{path/to/grubx64.efi}} {{[-C|--compression]}} xz {{normal}}`

- Display help:

`grub-mkimage {{[-?|--help]}}`

- Display version:

`grub-mkimage {{[-V|--version]}}`
