# մմ2գվ

> Փոխակերպեք գրաֆիկը Matrix Market `mm` ձևաչափից `gv` ձևաչափի:.
> Փոխարկիչներ՝ `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` և `mm2gv`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/mm2gv.1.pdf>:.

- Փոխակերպեք գրաֆիկը `mm`-ից `gv` ձևաչափի.:

`mm2gv -o {{output.gv}} {{input.mm}}`

- Փոխակերպեք գրաֆիկը՝ օգտագործելով `stdin` և `stdout`:

`cat {{input.mm}} | mm2gv > {{output.gv}}`

- Ցուցադրել օգնությունը.:

`mm2gv -?`
