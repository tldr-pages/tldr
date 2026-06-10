# pdf պատկեր

> PDF ֆայլերից պատկերներ հանելու օգտակար ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pdfimages>:.

- Բոլոր պատկերները հանեք PDF ֆայլից և պահեք դրանք որպես PNG:

`pdfimages -png {{path/to/file.pdf}} {{filename_prefix}}`

- Քաղեք պատկերներ 3-ից 5-րդ էջերից:

`pdfimages -f {{3}} -l {{5}} {{path/to/file.pdf}} {{filename_prefix}}`

- Արտահանեք պատկերներ PDF ֆայլից և ներառեք էջի համարը ելքային ֆայլերի անվանումներում.:

`pdfimages -p {{path/to/file.pdf}} {{filename_prefix}}`

- Թվարկեք տեղեկատվությունը բոլոր պատկերների մասին PDF ֆայլում.:

`pdfimages -list {{path/to/file.pdf}}`
