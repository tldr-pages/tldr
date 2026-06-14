# pbmկրճատել

> Համամասնականորեն կրճատեք PBM պատկերը:.
> Տես նաև՝ `pamenlarge`, `pamditherbw`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmreduce.html>:.

- Նվազեցրեք նշված պատկերը նշված գործոնով.:

`pbmreduce {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- Նվազեցնելիս օգտագործեք պարզ շեմը.:

`pbmreduce {{[-t|-threshold]}} {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- Օգտագործեք նշված շեմը բոլոր քվանտացումների համար.:

`pbmreduce {{[-va|-value]}} {{0.6}} {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`
