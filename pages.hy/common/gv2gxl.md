# gv2gxl

> Փոխակերպեք գրաֆիկը `gv`-ից `gxl` ձևաչափի:.
> Փոխարկիչներ՝ `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` և `mm2gv`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/gxl2gv.1.pdf>:.

- Փոխակերպեք գրաֆիկը `gv`-ից `gxl` ձևաչափի.:

`gv2gxl -o {{output.gxl}} {{input.gv}}`

- Փոխակերպեք գրաֆիկը՝ օգտագործելով `stdin` և `stdout`:

`cat {{input.gv}} | gv2gxl > {{output.gxl}}`

- Ցուցադրել օգնությունը.:

`gv2gxl -?`
