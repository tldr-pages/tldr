# kubectl uncordon

> Նշեք հանգույցը որպես պլանավորված՝ թույլ տալով նրան վերագրել նոր հանգույցներ:.
> Տես նաև՝ `kubectl cordon`:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_uncordon/>:.

- Նշեք հանգույցը որպես պլանավորված.:

`kubectl uncordon {{node_name}}`

- Նշեք բազմաթիվ հանգույցներ որպես պլանավորված.:

`kubectl uncordon {{node_name1 node_name2 ...}}`

- Նշեք հանգույցը որպես պլանավորված կոնկրետ համատեքստում.:

`kubectl uncordon {{node_name}} --context {{context_name}}`

- Նշեք պիտակի ընտրիչին համապատասխանող հանգույցները որպես պլանավորված.:

`kubectl uncordon {{[-l|--selector]}} {{label_key}}={{label_value}}`

- Նախադիտեք փոփոխությունները, առանց իրականում անջատելու հանգույցները (չոր վազք).:

`kubectl uncordon {{node_name}} --dry-run={{none|server|client}}`
