# gv2gml

> Conversia unui grafic din format `gv` în `gml`.
> Convertoare: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> Mai multe informaţii: <https://graphviz.org/pdf/gml2gv.1.pdf>

- Conversia unui grafic din format `gv` în `gml`:

`gv2gml -o {{output.gml}} {{input.gv}}`

- Conversia unui grafic folosind stdin și stdout:

`cat {{input.gv}} | gv2gml > {{output.gml}}`

- Ajutor pentru afișare:

`gv2gml -?`
