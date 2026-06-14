# macptopbm

> Կարդացեք MacPaint ֆայլը որպես մուտքագրում և ստացեք PBM պատկեր:.
> Տես նաև՝ `pbmtomacp`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/macptopbm.html>:.

- Փոխակերպեք MacPaint ֆայլը PGM պատկերի.:

`macptopbm {{path/to/file.macp}} > {{path/to/output.pbm}}`

- Ֆայլը կարդալիս բաց թողեք `n` բայթը՝:

`macptopbm {{[-e|-extraskip]}} {{n}} > {{path/to/output.pbm}}`

- Չեղարկել բոլոր տեղեկատվական հաղորդագրությունները.:

`macptopbm {{[-q|-quiet]}} > {{path/to/output.pbm}}`

- Ցուցադրման տարբերակը:

`macptopbm {{[-v|-version]}}`
