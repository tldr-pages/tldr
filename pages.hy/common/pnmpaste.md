#փնմպաստե

> Տեղադրեք PNM պատկերը մեկ այլ PNM պատկերի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmpaste.html>:.

- Տեղադրեք PNM պատկերը մեկ այլ PNM պատկերի մեջ նշված կոորդինատներով.:

`pnmpaste {{x}} {{y}} {{path/to/image1.pnm}} {{path/to/image2.pnm}} > {{path/to/output.pnm}}`

- Տեղադրեք `stdin`-ից կարդացված պատկերը նշված պատկերի մեջ.:

`{{command}} | pnmpaste {{x}} {{y}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Միավորել համընկնող պիքսելները նշված բուլյան գործողությամբ, որտեղ սպիտակ պիքսելները ներկայացնում են `true`, մինչդեռ սև պիքսելները ներկայացնում են `false`:

`pnmpaste -{{and|nand|or|nor|xor|xnor}} {{x}} {{y}} {{path/to/image1.pnm}} {{path/to/image2.pnm}} > {{path/to/output.pnm}}`
