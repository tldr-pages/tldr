# chkfont

> Verify the format of a FIGlet font file (`.flf`).
> See also: `figlet`, `figlist`, `showfigfonts`.
> More information: <https://linux.die.net/man/6/chkfont>.

- Check a font file for formatting errors:

`chkfont {{path/to/font.flf}}`

- Check all `.flf` font files in a directory:

`for font in {{path/to/fonts}}/*.flf; do chkfont "$font"; done`
