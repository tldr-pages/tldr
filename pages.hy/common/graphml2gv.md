# graphml2gv

> Փոխակերպեք գրաֆիկը `graphml`-ից `gv` ձևաչափի:.
> Փոխարկիչներ՝ `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` և `mm2gv`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/graphml2gv.1.pdf>:.

- Փոխակերպեք գրաֆիկը `gml`-ից `gv` ձևաչափի.:

`graphml2gv -o {{output.gv}} {{input.gml}}`

- Փոխակերպեք գրաֆիկը՝ օգտագործելով `stdin` և `stdout`:

`cat {{input.gml}} | graphml2gv > {{output.gv}}`

- Ցուցադրել օգնությունը.:

`graphml2gv -?`
