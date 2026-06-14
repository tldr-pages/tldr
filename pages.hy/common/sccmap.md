# sccmap

> Արդյունահանեք ուղղորդված գրաֆիկների ամուր կապված բաղադրիչները:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://www.graphviz.org/pdf/sccmap.1.pdf>:.

- Արտահանեք մեկ կամ մի քանի ուղղորդված գրաֆիկների ամուր կապված բաղադրիչներ.:

`sccmap -S {{path/to/input1.gv path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Տպել վիճակագրություն գրաֆիկի մասին՝ չարտադրելով ելքային գրաֆիկ.:

`sccmap -v -s {{path/to/input1.gv path/to/input2.gv ...}}`

- Ցուցադրել օգնությունը.:

`sccmap -?`
