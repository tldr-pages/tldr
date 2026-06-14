# gml2gv

> Փոխակերպեք գրաֆիկը `gml`-ից `gv` ձևաչափի:.
> Փոխարկիչներ՝ `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` և `mm2gv`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/gml2gv.1.pdf>:.

- Փոխակերպեք գրաֆիկը `gml`-ից `gv` ձևաչափի.:

`gml2gv -o {{output.gv}} {{input.gml}}`

- Փոխակերպեք գրաֆիկը՝ օգտագործելով `stdin` և `stdout`:

`cat {{input.gml}} | gml2gv > {{output.gv}}`

- Ցուցադրել օգնությունը.:

`gml2gv -?`
