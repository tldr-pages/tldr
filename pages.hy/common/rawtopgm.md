# rawtopgm

> Վերափոխեք չմշակված մոխրագույն մասշտաբի պատկերը PGM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/rawtopgm.html>:.

- Վերափոխեք չմշակված մոխրագույն մասշտաբի պատկերը PGM պատկերի.:

`rawtopgm {{width}} {{height}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Վերափոխեք չմշակված մոխրագույն մասշտաբի պատկերը PGM պատկերի, ենթադրեք, որ պատկերը քառակուսի է.:

`rawtopgm {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Վերափոխեք չմշակված մոխրագույն մասշտաբի պատկերը, որտեղ պիքսելները առաջինը ներքևում են, ոչ թե վերևից առաջինը, PGM պատկերի:

`rawtopgm {{width}} {{height}} {{[-bt|-bottomfirst]}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Անտեսեք նշված ֆայլի առաջին `n` բայթերը.:

`rawtopgm {{width}} {{height}} {{[-h|-headerskip]}} {{n}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Անտեսեք նշված ֆայլի յուրաքանչյուր տողի վերջին մ բայթերը.:

`rawtopgm {{width}} {{height}} {{[-r|-rowskip]}} {{m}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Նշեք մուտքագրման մեջ մոխրագույն արժեքների առավելագույն արժեքը, որպեսզի հավասար լինի `n`-ին:

`rawtopgm {{width}} {{height}} {{[-m|-maxval]}} {{n}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Նշեք բայթերի քանակը, որոնք ներկայացնում են յուրաքանչյուր նմուշ մուտքագրման մեջ, և որ բայթերի հաջորդականությունը պետք է մեկնաբանվի որպես քիչ էնդյան:

`rawtopgm {{width}} {{height}} -bpp {{1|2}} {{[-l|-littleendian]}} {{path/to/image.raw}} > {{path/to/output.pgm}}`
