# acyclic

> Haz un gráfico acíclico invirtiendo algunos bordes.
> Filtros Graphviz: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> Más información: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Haz un gráfico acíclico invirtiendo algunos bordes:

`acyclic {{ruta/a/entrada.gv}} > {{ruta/a/salida.gv}}`

- Imprime si un gráfico es acíclico, tiene un ciclo o si no posee instrucciones, no genera ningún gráfico de salida:

`acyclic -v -n {{ruta/a/entrada.gv}}`

- Muestra información de ayuda:

`acyclic -?`
