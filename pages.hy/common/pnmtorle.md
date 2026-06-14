# pnmtorle

> Փոխարկել PNM ֆայլը Utah Raster Tools RLE պատկերի ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtorle.html>:.

- Փոխակերպեք PNM պատկերը RLE պատկերի.:

`pnmtorle {{path/to/input.pnm}} > {{path/to/output.rle}}`

- Տպել PNM վերնագրի տեղեկությունները `stdout`-ում:

`pnmtorle {{[-verb|-verbose]}} {{path/to/input.pnm}} > {{path/to/output.rle}}`

- Ներառեք թափանցիկության ալիք ելքային պատկերում, որում յուրաքանչյուր սև պիքսել դրված է լիովին թափանցիկ, իսկ յուրաքանչյուր այլ պիքսել՝ ամբողջովին անթափանց:

`pnmtorle {{[-a|-alpha]}} {{path/to/input.pnm}} > {{path/to/output.rle}}`
