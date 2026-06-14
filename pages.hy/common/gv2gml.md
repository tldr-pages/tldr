# gv2gml

> Փոխակերպեք գրաֆիկը `gv`-ից `gml` ձևաչափի:.
> Փոխարկիչներ՝ `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` և `mm2gv`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/gml2gv.1.pdf>:.

- Փոխակերպեք գրաֆիկը `gv`-ից `gml` ձևաչափի.:

`gv2gml -o {{output.gml}} {{input.gv}}`

- Փոխակերպեք գրաֆիկը՝ օգտագործելով `stdin` և `stdout`:

`cat {{input.gv}} | gv2gml > {{output.gml}}`

- Ցուցադրել օգնությունը.:

`gv2gml -?`
