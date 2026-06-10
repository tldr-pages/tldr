#խառնվել

> Փաթեթավորեք գրաֆիկի դասավորության եզրերը:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://www.graphviz.org/pdf/mingle.1.pdf>:.

- Միավորել մեկ կամ մի քանի գրաֆիկի դասավորության եզրերը (որոնք արդեն ունեն դասավորության մասին տեղեկատվություն).:

`mingle {{path/to/layout1.gv path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Կատարեք դասավորություն, փաթեթավորում և նկարի դուրսբերում մեկ հրամանով.:

`dot {{path/to/input.gv}} | mingle | dot -T {{png}} > {{path/to/output.png}}`

- Ցուցադրել օգնությունը.:

`mingle -?`
