#չհարթեցված

> Կարգավորեք ուղղորդված գրաֆիկները՝ դասավորության հարաբերակցությունը բարելավելու համար:.
> Graphviz զտիչներ՝ `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, __IN_LINE_CODE_6__, __IN_LINE_CO, `tred` և `unflatten`:.
> Լրացուցիչ տեղեկություններ. <https://www.graphviz.org/pdf/unflatten.1.pdf>:.

- Կարգավորեք մեկ կամ մի քանի ուղղորդված գրաֆիկներ՝ դասավորության հարաբերակցությունը բարելավելու համար.:

`unflatten {{path/to/input1.gv path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Օգտագործեք `unflatten`-ը որպես նախապրոցեսոր `dot` դասավորության համար՝ հարթության հարաբերակցությունը բարելավելու համար:

`unflatten {{path/to/input.gv}} | dot -T {{png}} {{path/to/output.png}}`

- Ցուցադրել օգնությունը.:

`unflatten -?`
