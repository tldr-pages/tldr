# gv2gxl

> Conversia unui grafic din formatul `gv` în `gxl`.
> Convertoare: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> Mai multe informaţii: <https://graphviz.org/pdf/gxl2gv.1.pdf>

- Conversia unui grafic din formatul `gv` în `gxl`:

`gv2gxl -o {{output.gxl}} {{input.gv}}`

- Conversia unui grafic folosind stdin și stdout:

`cat {{input.gv}} | gv2gxl > {{output.gxl}}`

- Ajutor pentru afișare:

`gv2gxl -?`
