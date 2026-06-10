# gvcolor

> Գունավորե՛ք դասակարգված երկգրաֆիկը մի շարք գույներով:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/gvcolor.1.pdf>:.

- Գունավորեք մեկ կամ մի քանի դասակարգված երկգրաֆիկ (որոնք արդեն մշակվել են `dot`-ի կողմից):

`gvcolor {{path/to/layout1.gv path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Դրեք գրաֆիկ և գունավորեք այն, այնուհետև փոխարկեք PNG պատկերի.:

`dot {{path/to/input.gv}} | gvcolor | dot -T {{png}} > {{path/to/output.png}}`

- Ցուցադրել օգնությունը.:

`gvcolor -?`
