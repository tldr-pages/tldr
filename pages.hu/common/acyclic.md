# acyclic

> Egy irányított gráf aciklikussá tétele néhány él megfordításával. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: [https://graphviz.org/pdf/acyclic.1.pdf.](https://graphviz.org/pdf/acyclic.1.pdf)

- Néhány él megfordításával tegyen egy irányított gráfot aciklikussá:

`acyclic {{path/to/input.gv}} > {{path/to/output.gv}}`

- Nyomtassa ki, hogy egy gráf aciklikus-e, van-e ciklusa, vagy nem irányított, és ne adjon ki kimeneti gráfot:

`acyclic -v -n {{path/to/input.gv}}`

- A `acyclic` súgójának megjelenítése:

`acyclic -?`
