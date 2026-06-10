# bcomps

> Գրաֆիկները տարրալուծեք իրենց երկկողմանի բաղադրիչների մեջ:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/bcomps.1.pdf>:.

- Մեկ կամ մի քանի գծապատկերներ տարրալուծեք իրենց երկկողմանի բաղադրիչների մեջ.:

`bcomps {{path/to/input1.gv path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Տպեք բլոկների և կտրվածքների քանակը մեկ կամ մի քանի գրաֆիկներում.:

`bcomps -v -s {{path/to/input1.gv path/to/input2.gv ...}}`

- Գրեք յուրաքանչյուր բլոկ և բլոկ-cutvertex ծառ մի քանի համարակալված ֆայլերի անուններում՝ հիմնված `output.gv`-ի վրա:

`bcomps -x -o {{path/to/output.gv}} {{path/to/input1.gv path/to/input2.gv ...}}`

- Ցուցադրել օգնությունը.:

`bcomps -?`
