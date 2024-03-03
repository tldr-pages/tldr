# pamtogif

> Convert a Netpbm image into an unanimated GIF image.
> See also: `giftopnm`, `gifsicle`.
> More information: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Convert a Netpbm image into an unanimated GIF image:

`pamtogif {{path/to/image.pam}} > {{path/to/output.gif}}`

- Mark the specified color as transparent in the output GIF file:

`pamtogif -transparent {{color}} {{path/to/image.pam}} > {{path/to/output.gif}}`

- Include the specified text as a comment in the output GIF file:

`pamtogif -comment "{{Hello World!}}" {{path/to/image.pam}} > {{path/to/output.gif}}`
