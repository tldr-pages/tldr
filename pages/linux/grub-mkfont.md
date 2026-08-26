# grub-mkfont

> Convert common font file formats into the PF2 format used by GRUB.
> More information: <https://manpages.debian.org/latest/grub2-common/grub-mkfont.1.en.html>.

- Convert a font to PF2:

`grub-mkfont --output {{path/to/output.pf2}} {{path/to/font.ttf}}`

- Convert a font at a specific size:

`grub-mkfont --size {{24}} --output {{path/to/output.pf2}} {{path/to/font.ttf}}`

- Convert only characters in specific Unicode ranges:

`grub-mkfont --range {{0x20-0x7E,0xA0-0xFF}} --output {{path/to/output.pf2}} {{path/to/font.ttf}}`

- Set the output font family name:

`grub-mkfont --name "{{font_family_name}}" --output {{path/to/output.pf2}} {{path/to/font.ttf}}`

- Convert a font to bold while forcing automatic hinting:

`grub-mkfont --bold --force-autohint --output {{path/to/output.pf2}} {{path/to/font.ttf}}`

- Disable hinting and ignore embedded bitmap strikes:

`grub-mkfont --no-hinting --no-bitmap --output {{path/to/output.pf2}} {{path/to/font.ttf}}`
