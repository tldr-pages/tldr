# gxl2gv

> Conversia unui grafic din formatul `gxl` în `gv`.
> Convertoare: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> Mai multe informaţii: <https://graphviz.org/pdf/gxl2gv.1.pdf>

- Conversia unui grafic din formatul `gxl` în `gv`:

`gxl2gv -o {{output.gv}} {{input.gxl}}`

- Conversia unui grafic folosind stdin și stdout:

`cat {{input.gxl}} | gxl2gv > {{output.gv}}`

- Ajutor pentru afișare:

`gxl2gv -?`
