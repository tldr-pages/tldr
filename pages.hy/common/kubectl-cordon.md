# kubectl կորդոն

> Նշեք հանգույցը որպես չպլանավորված՝ թույլ չտալով նոր հանգույցներ հատկացնել նրան:.
> Տես նաև՝ `kubectl uncordon`:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/>:.

- Նշեք հանգույցը որպես չպլանավորված.:

`kubectl cordon {{node_name}}`

- Նշեք բազմաթիվ հանգույցներ որպես չպլանավորված.:

`kubectl cordon {{node_name1 node_name2 ...}}`

- Նշեք հանգույցը որպես չպլանավորված կոնկրետ համատեքստում.:

`kubectl cordon {{node_name}} --context {{context_name}}`

- Նշել պիտակի ընտրիչին համապատասխանող հանգույցները որպես չպլանավորված.:

`kubectl cordon {{[-l|--selector]}} {{label_key}}={{label_value}}`

- Նախադիտեք փոփոխությունները՝ առանց իրականում շրջափակելու հանգույցները (չոր վազք).:

`kubectl cordon {{node_name}} --dry-run={{none|server|client}}`
