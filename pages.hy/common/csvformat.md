# csv ձևաչափ

> Փոխակերպեք CSV ֆայլը մաքսային ելքային ձևաչափի:.
> Ներառված է csvkit-ում:.
> Լրացուցիչ տեղեկություններ. <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>:.

- Փոխարկել ներդիրներով սահմանազատված ֆայլի (TSV).:

`csvformat {{[-T|--out-tabs]}} {{data.csv}}`

- Փոխակերպեք սահմանազատիչները հատուկ նիշի.:

`csvformat {{[-D|--out-delimiter]}} "{{custom_character}}" {{data.csv}}`

- Փոխարկել տողերի վերջավորությունները փոխադրման վերադարձի (^M) + տողերի սնուցման.:

`csvformat {{[-M|--out-lineterminator]}} "{{\r\n}}" {{data.csv}}`

- Նվազեցրեք մեջբերումների նիշերի օգտագործումը.:

`csvformat {{[-U|--out-quoting]}} 0 {{data.csv}}`

- Առավելագույնի հասցնել մեջբերումների նիշերի օգտագործումը.:

`csvformat {{[-U|--out-quoting]}} 1 {{data.csv}}`
