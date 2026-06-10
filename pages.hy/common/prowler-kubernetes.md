# prowler kubernetes

> Գնահատեք Kubernetes կլաստերի անվտանգության լավագույն փորձը և կազմաձևերը:.
> Տես նաև՝ `prowler`, `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-m365`, `prowler-github`:.
> Լրացուցիչ տեղեկություններ. <https://docs.prowler.com/user-guide/cli/tutorials/misc>:.

- Գործարկեք լռելյայն ստուգումները՝ օգտագործելով լռելյայն kubeconfig տեղադրությունը.:

`prowler kubernetes`

- Նշեք հատուկ kubeconfig ֆայլ սկանավորման համար.:

`prowler kubernetes --kubeconfig-file {{path/to/kubeconfig}}`

- Նշեք հատուկ Kubernetes համատեքստ սկանավորման համար.:

`prowler kubernetes --context {{my-context}}`

- Սկանավորեք միայն հատուկ անունների տարածքներ.:

`prowler kubernetes --namespaces {{default}} {{kube-system}}`

- Կատարեք ստուգումներ ընտրված Kubernetes ծառայությունների համար.:

`prowler kubernetes {{[-s|--services]}} {{ietcd|apiserver|...}}`

- Գործարկել հատուկ Kubernetes ստուգում.:

`prowler kubernetes {{[-c|--checks]}} {{etcd_encryption}}`

- Բացառել հատուկ ստուգումներ կամ ծառայություններ.:

`prowler kubernetes {{[-e|--excluded-checks]}} {{etcd_encryption}} --exclude-services {{ietcd|apiserver|...}}`
