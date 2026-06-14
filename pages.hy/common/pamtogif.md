# pamtogif

> Փոխակերպեք Netpbm պատկերը անիմացիոն GIF պատկերի:.
> Տես նաև՝ `giftopnm`, `gifsicle`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamtogif.html>:.

- Netpbm պատկերը վերածեք անիմացիոն GIF պատկերի.:

`pamtogif {{path/to/image.pam}} > {{path/to/output.gif}}`

- Նշեք նշված գույնը որպես թափանցիկ ելքային GIF ֆայլում.:

`pamtogif {{[-t|-transparent]}} {{color}} {{path/to/image.pam}} > {{path/to/output.gif}}`

- Ներառեք նշված տեքստը որպես մեկնաբանություն ելքային GIF ֆայլում.:

`pamtogif {{[-c|-comment]}} "{{Hello World!}}" {{path/to/image.pam}} > {{path/to/output.gif}}`
