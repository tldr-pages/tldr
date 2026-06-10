# rawtoppm

> Վերափոխեք չմշակված RGB հոսքը PPM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/rawtoppm.html>:.

- Հում RGB հոսքը փոխարկեք PPM պատկերի.:

`rawtoppm {{width}} {{height}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- Փոխակերպեք չմշակված RGB հոսքը, որտեղ պիքսելները առաջինը ներքևում են՝ վերևից առաջինի փոխարեն, PPM պատկերի:

`rawtoppm {{width}} {{height}} {{path/to/image.raw}} | pamflip {{[-tb|-topbottom]}} > {{path/to/output.ppm}}`

- Անտեսեք նշված ֆայլի առաջին n բայթը.:

`rawtoppm {{width}} {{height}} {{[-h|-headerskip]}} {{n}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- Անտեսեք նշված ֆայլի յուրաքանչյուր տողի վերջին մ բայթերը.:

`rawtoppm {{width}} {{height}} {{[-ro|-rowskip]}} {{m}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- Նշեք գունային բաղադրիչների հերթականությունը յուրաքանչյուր պիքսելի համար.:

`rawtoppm {{width}} {{height}} -{{rgb|rbg|grb|gbr|brg|bgr}} {{path/to/image.raw}} > {{path/to/output.ppm}}`
