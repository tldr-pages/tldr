# acyclic

> Rendi un grafo diretto aciclico invertendo alcuni archi.
> Filtri Graphviz: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, e `unflatten`.
> Maggiori informazioni: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Rendi un grafo diretto aciclico invertendo alcuni archi:

`acyclic {{percorso/a/input.gv}} > {{percorso/a/output.gv}}`

- Stampa se un grafo è aciclico, ha un ciclo, o è non orientato, senza produrre grafo in output:

`acyclic -v -n {{percorso/a/input.gv}}`

- Visualizza l'aiuto:

`acyclic -?`
