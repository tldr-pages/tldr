# grub-mkfont

> Convert common font file formats into the PF2 format used by GRUB.
> More information: <https://manned.org/grub-mkfont>.

- Convert a font to PF2:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{path/to/font.ttf}}`

- Convert a font at a specific size:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-s|--size]}} {{24}} {{path/to/font.ttf}}`

- Convert only characters in specific Unicode ranges:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-r|--range]}} {{0x20-0x7E,0xA0-0xFF}} {{path/to/font.ttf}}`

- Set the output font family name:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-n|--name]}} "{{font_family_name}}" {{path/to/font.ttf}}`

- Convert a font to bold while forcing automatic hinting:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-b|--bold]}} {{[-a|--force-autohint]}} {{path/to/font.ttf}}`

- Disable hinting and ignore embedded bitmap strikes:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} --no-hinting --no-bitmap {{path/to/font.ttf}}`
