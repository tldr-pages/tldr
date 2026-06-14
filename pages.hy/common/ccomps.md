# կոմպ

> Գրաֆիկները տարրալուծել իրենց միացված բաղադրիչների:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/ccomps.1.pdf>:.

- Մեկ կամ մի քանի գծապատկերներ տարրալուծել իրենց միացված բաղադրիչների.:

`ccomps {{path/to/input1.gv path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Տպեք հանգույցների, եզրերի և միացված բաղադրիչների քանակը մեկ կամ մի քանի գրաֆիկներում.:

`ccomps -v -s {{path/to/input1.gv path/to/input2.gv ...}}`

- Յուրաքանչյուր միացված բաղադրիչ գրեք համարակալված ֆայլերի անուններում՝ հիմնված `output.gv`-ի վրա:

`ccomps -x -o {{path/to/output.gv}} {{path/to/input1.gv path/to/input2.gv ...}}`

- Ցուցադրել օգնությունը.:

`ccomps -?`
