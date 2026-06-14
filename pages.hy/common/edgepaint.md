# եզրային ներկ

> Գունավորեք գրաֆիկի դասավորության եզրերը՝ խաչվող եզրերը պարզաբանելու համար:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/edgepaint.1.pdf>:.

- Գունավորեք մեկ կամ մի քանի գծապատկերների դասավորության եզրերը (որոնք արդեն ունեն դասավորության տեղեկատվություն)՝ հատվող եզրերը պարզաբանելու համար.:

`edgepaint {{path/to/layout1.gv path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Գունավորեք եզրերը՝ օգտագործելով գունային սխեման: (Տես <https://graphviz.org/doc/info/colors.html#brewer>):

`edgepaint -color-scheme={{accent7}} {{path/to/layout.gv}} > {{path/to/output.gv}}`

- Դրեք գրաֆիկ և գունավորեք դրա եզրերը, այնուհետև փոխարկեք PNG պատկերի.:

`dot {{path/to/input.gv}} | edgepaint | dot -T {{png}} > {{path/to/output.png}}`

- Ցուցադրել օգնությունը.:

`edgepaint -?`
