# acyclic

> Maak een gerichte grafiek acyclisch door enkele randen om te keren.
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> Meer informatie: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Maak een gerichte grafiek acyclisch door enkele randen om te keren:

`acyclic {{pad/naar/invoer.gv}} > {{pad/naar/uitvoer.gv}}`

- Afdrukken als een grafiek acyclisch is, een cyclus heeft of ongericht is en geen uitvoergrafiek produceert:

`acyclic -v -n {{pad/naar/invoer.gv}}`

- Toon de help:

`acyclic -?`
