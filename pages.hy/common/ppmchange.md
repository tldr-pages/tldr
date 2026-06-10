# ppmփոփոխություն

> Փոխեք մեկ գույնի բոլոր պիքսելները PPM պատկերի մեկ այլ գույնի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmchange.html>:.

- Փոխանակեք առաջին գույնը յուրաքանչյուր `oldcolor` - `newcolor` զույգի երկրորդ գույնի հետ.:

`ppmchange {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- Նշեք, թե որքան նման գույներ պետք է լինեն, որպեսզի նույնը համարվեն.:

`ppmchange -closeness {{percentage}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- Փոխարինեք արգումենտներում չնշված բոլոր պիքսելները գույնով.:

`ppmchange {{[-r|-remainder]}} {{color}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`
