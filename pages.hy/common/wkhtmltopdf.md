# wkhtmltopdf

> Փոխակերպեք HTML փաստաթղթերը կամ վեբ էջերը PDF ֆայլերի:.
> Լրացուցիչ տեղեկություններ. <https://wkhtmltopdf.org/usage/wkhtmltopdf.txt>:.

- Փոխակերպեք HTML փաստաթուղթը PDF-ի.:

`wkhtmltopdf {{input.html}} {{output.pdf}}`

- Նշեք PDF էջի չափը (աջակցվող չափերի համար տես `PaperSize`-ը `QPrinter`-ից):

`wkhtmltopdf --page-size {{A4}} {{input.html}} {{output.pdf}}`

- Սահմանեք PDF էջի լուսանցքները.:

`wkhtmltopdf --margin-{{top|bottom|left|right}} {{10mm}} {{input.html}} {{output.pdf}}`

- Սահմանեք PDF էջի կողմնորոշումը.:

`wkhtmltopdf --orientation {{Landscape|Portrait}} {{input.html}} {{output.pdf}}`

- Ստեղծեք PDF փաստաթղթի մոխրագույն տարբերակ.:

`wkhtmltopdf --grayscale {{input.html}} {{output.pdf}}`
