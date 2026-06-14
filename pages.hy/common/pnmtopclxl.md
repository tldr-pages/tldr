# pnmtopclxl

> Փոխարկեք PNM ֆայլը HP LaserJet PCL XL տպիչի հոսքի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtopclxl.html>:.

- Փոխարկեք PNM ֆայլերը HP LaserJet PCL XL տպիչի հոսքի.:

`pnmtopclxl {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- Յուրաքանչյուր պատկերի վերին ձախ անկյունից նշեք պատկերի լուծումը, ինչպես նաև էջի գտնվելու վայրը.:

`pnmtopclxl -dpi {{resolution}} {{[-x|-xoffs]}} {{x_offset}} {{[-y|-yoffs]}} {{y_offset}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- Ստեղծեք կրկնակի տպիչի հոսք նշված թղթի ձևաչափի համար.:

`pnmtopclxl {{[-du|-duplex]}} {{vertical|horizontal}} {{[-fo|-format]}} {{letter|legal|a3|a4|a5|...}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`
