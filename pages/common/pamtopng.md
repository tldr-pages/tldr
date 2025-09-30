# pamtopng

> Convert a PAM image to PNG.
> See also: `pnmtopng`, `pngtopam`.
> More information: <https://netpbm.sourceforge.net/doc/pamtopng.html>.

- Convert the specified PAM image to PNG:

`pamtopng {{path/to/image.pam}} > {{path/to/output.png}}`

- Mark the specified color as transparent in the output image:

`pamtopng {{[-t|-transparent]}} {{color}} {{path/to/image.pam}} > {{path/to/output.png}}`

- Include the text in the specified file as tEXt chunks in the output:

`pamtopng {{[-te|-text]}} {{path/to/file.txt}} {{path/to/image.pam}} > {{path/to/output.png}}`

- Cause the output file to be interlaced in Adam7 format:

`pamtopng {{[-in|-interlace]}} {{path/to/image.pam}} > {{path/to/output.png}}`
