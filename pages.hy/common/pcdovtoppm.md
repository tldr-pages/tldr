# pcdovtoppm

> Ստեղծեք ինդեքսային պատկեր ֆոտո CD-ի համար՝ հիմնվելով դրա ընդհանուր ֆայլի վրա:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>:.

- Ստեղծեք PPM ինդեքսի պատկեր PCD ընդհանուր ֆայլից.:

`pcdovtoppm {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- Նշեք ելքային պատկերի առավելագույն լայնությունը և ելքում պարունակվող յուրաքանչյուր պատկերի առավելագույն չափը.:

`pcdovtoppm {{[-m|-maxwidth]}} {{width}} {{[-s|-size]}} {{size}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- Նշեք պատկերների առավելագույն քանակը և գույների առավելագույն քանակը.:

`pcdovtoppm {{[-a|-across]}} {{n_images}} {{[-c|-colors]}} {{n_colours}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- Անոտացիաների համար օգտագործեք նշված տառատեսակը և ֆոնը սպիտակ ներկեք.:

`pcdovtoppm {{[-f|-font]}} {{font}} {{[-w|-white]}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`
