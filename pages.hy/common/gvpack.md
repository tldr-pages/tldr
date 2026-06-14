# gvpack

> Միավորել գրաֆիկի մի քանի դասավորություններ (որոնք արդեն ունեն դասավորության տեղեկատվություն):.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/gvpack.1.pdf>:.

- Միավորել գրաֆիկի մի քանի դասավորություններ (որոնք արդեն ունեն դասավորության տեղեկատվություն).:

`gvpack {{path/to/layout1.gv path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Միավորել գրաֆիկի մի քանի դասավորություններ գրաֆիկի մակարդակում՝ գրաֆիկները առանձին պահելով.:

`gvpack -g {{path/to/layout1.gv path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Միավորել մի քանի գրաֆիկական դասավորություններ հանգույցի մակարդակում՝ անտեսելով կլաստերները.:

`gvpack -n {{path/to/layout1.gv path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Միավորել մի քանի գրաֆիկական դասավորություններ առանց փաթեթավորման.:

`gvpack -u {{path/to/layout1.gv path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Ցուցադրել օգնությունը.:

`gvpack -?`
