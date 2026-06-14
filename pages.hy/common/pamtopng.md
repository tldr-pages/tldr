# pamtopng

> Փոխարկել PAM պատկերը PNG-ի:.
> Տես նաև՝ `pnmtopng`, `pngtopam`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamtopng.html>:.

- Նշված PAM պատկերը փոխարկեք PNG.:

`pamtopng {{path/to/image.pam}} > {{path/to/output.png}}`

- Նշված գույնը նշեք որպես թափանցիկ ելքային պատկերում.:

`pamtopng {{[-t|-transparent]}} {{color}} {{path/to/image.pam}} > {{path/to/output.png}}`

- Ներառեք տեքստը նշված ֆայլում որպես տեքստային կտորներ ելքի մեջ.:

`pamtopng {{[-te|-text]}} {{path/to/file.txt}} {{path/to/image.pam}} > {{path/to/output.png}}`

- Ստիպեք ելքային ֆայլը միահյուսվել Adam7 ձևաչափով.:

`pamtopng {{[-in|-interlace]}} {{path/to/image.pam}} > {{path/to/output.png}}`
