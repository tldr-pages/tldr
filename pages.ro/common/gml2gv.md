# gml2gv

> Conversia unui grafic din format `gml` în `gv`.
> Convertoare: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> Mai multe informaţii: <https://graphviz.org/pdf/gml2gv.1.pdf>

- Conversia unui grafic din format `gml` în `gv`:

`gml2gv -o {{output.gv}} {{input.gml}}`

- Conversia unui grafic folosind stdin și stdout:

`cat {{input.gml}} | gml2gv > {{output.gv}}`

- Ajutor pentru afișare:

`gml2gv -?`
