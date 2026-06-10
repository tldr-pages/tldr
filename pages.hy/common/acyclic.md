# ացիկլիկ

> Ուղղորդված գրաֆիկը դարձրեք ացիկլիկ՝ շրջելով որոշ եզրեր:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://graphviz.org/pdf/acyclic.1.pdf>:.

- Ուղղորդված գծապատկերը դարձրեք ացիկլիկ՝ շրջելով որոշ եզրեր.:

`acyclic {{path/to/input.gv}} > {{path/to/output.gv}}`

- Տպել, եթե գրաֆիկը ացիկլիկ է, ունի ցիկլ կամ անուղղորդված է, որը չի արտադրում ելքային գրաֆիկ.:

`acyclic -v -n {{path/to/input.gv}}`

- Ցուցադրել օգնությունը.:

`acyclic -?`
