# grub-mkrescue

> Make a GRUB CD/USB/floppy bootable image.
> More information: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmkrescue>.

- Create a bootable ISO from the current directory and save it as `grub.iso`:

`grub-mkrescue --output {{grub.iso}} .`

- Create an ISO using GRUB files from a custom directory:

`grub-mkrescue --directory {{/usr/lib/grub/i386-pc}} --output {{grub.iso}} {{path/to/source}}`

- Use compression for GRUB files when building the image, setting `no` disables compression:

`grub-mkrescue --compress {{no|xz|gz|lzo}} --output {{grub.iso}} {{path/to/source}}`

- Disable the GRUB command-line interface in the generated image:

`grub-mkrescue --disable-cli --output {{grub.iso}} {{path/to/source}}`

- Preload specific GRUB modules into the image:

`grub-mkrescue --modules "{{part_gpt iso9660}}" --output {{grub.iso}} {{path/to/source}}`

- Pass additional options directly to `xorriso`:

`grub-mkrescue --output {{grub.iso}} -- {{-volid}} {{volume_name}} {{path/to/source}}`

- Display help:

`grub-mkrescue {{[-?|--help]}}`

- Display version:

`grub-mkrescue --version`
