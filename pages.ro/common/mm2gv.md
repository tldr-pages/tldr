# mm2gv

> Conversia unui grafic din formatul Matrix Market `mm` în format `gv`.
> Convertoare: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
> Mai multe informaţii: <https://graphviz.org/pdf/mm2gv.1.pdf>

- Conversia unui grafic din format `mm` în `gv`:

`mm2gv -o {{output.gv}} {{input.mm}}`

- Conversia unui grafic folosind stdin și stdout:

`cat {{input.mm}} | mm2gv > {{output.gv}}`

- Ajutor pentru afișare:

`mm2gv -?`
