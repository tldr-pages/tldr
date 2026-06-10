# ilbmtoppm

> Փոխակերպեք ILBM ֆայլը PPM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ilbmtoppm.html>:.

- Փոխակերպեք ILBM ֆայլը PPM պատկերի.:

`ilbmtoppm {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- Օգտագործեք նշված գույնը՝ «ցույց տալով», որտեղ պատկերը թափանցիկ է.:

`ilbmtoppm {{[-t|-transparent]}} {{color}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- Անտեսեք հատվածը նշված հատվածի ID-ով.:

`ilbmtoppm {{[-ig|-ignore]}} {{chunk_id}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- Պահպանեք մուտքագրման թափանցիկության տեղեկատվությունը նշված PBM ֆայլում.:

`ilbmtoppm {{[-m|-maskfile]}} {{path/to/maskfile.pbm}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`
