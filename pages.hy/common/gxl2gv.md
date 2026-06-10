# gxl2gv

> Փոխակերպեք գրաֆիկը `gxl`-ից `gv` ձևաչափի:.
> Փոխարկիչներ՝ `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` և `mm2gv`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/gxl2gv.1.pdf>:.

- Փոխակերպեք գրաֆիկը `gxl`-ից `gv` ձևաչափի.:

`gxl2gv -o {{output.gv}} {{input.gxl}}`

- Փոխակերպեք գրաֆիկը՝ օգտագործելով `stdin` և `stdout`:

`cat {{input.gxl}} | gxl2gv > {{output.gv}}`

- Ցուցադրել օգնությունը.:

`gxl2gv -?`
