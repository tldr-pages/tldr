# mutool

> Փոխակերպել, հարցումներ փնտրել և տվյալների հանել PDF ֆայլերից:.
> Լրացուցիչ տեղեկություններ. <https://mupdf.readthedocs.io/en/latest/tools/mutool.html>:.

- Փոխակերպեք մի շարք էջեր PNG-ի (Նշում. `%nd` ելքային տեղապահում պետք է փոխարինվի տպման փոփոխիչով, ինչպիսին է `%d` կամ `%2d`):

`mutool convert -o {{path/to/output%nd.png}} {{path/to/input.pdf}} {{1-10}}`

- Փոխակերպեք PDF-ի մեկ կամ մի քանի էջ տեքստի `stdout`-ով՝:

`mutool draw -F txt {{path/to/input.pdf}} {{2,3,5,...}}`

- Միավորել բազմաթիվ PDF ֆայլեր.:

`mutool merge -o {{path/to/output.pdf}} {{path/to/input1.pdf path/to/input2.pdf ...}}`

- Հարցրեք տեղեկատվություն PDF-ում ներկառուցված ամբողջ բովանդակության մասին.:

`mutool info {{path/to/input.pdf}}`

- PDF-ում ներկառուցված բոլոր պատկերները, տառատեսակները և ռեսուրսները հանեք ընթացիկ գրացուցակում.:

`mutool extract {{path/to/input.pdf}}`

- Ցույց տալ PDF-ի ուրվագիծը (բովանդակության աղյուսակը).:

`mutool show {{path/to/input.pdf}} outline`
