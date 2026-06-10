# kubectl կազմաձևում

> Կառավարեք Kubernetes-ի կազմաձևման (kubeconfig) ֆայլերը՝ `kubectl`-ի կամ Kubernetes API-ի միջոցով կլաստերներ մուտք գործելու համար:.
> Լռելյայնորեն, Kubernetes-ը կստանա իր կոնֆիգուրացիան `${HOME}/.kube/config`-ից:.
> Տես նաև՝ `kubectx`, `kubens`:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_config/>:.

- Ստացեք բոլոր համատեքստերը լռելյայն kubeconfig ֆայլում.:

`kubectl config get-contexts`

- Ստացեք բոլոր կլաստերները / համատեքստերը / օգտվողները հատուկ kubeconfig ֆայլում.:

`kubectl config {{get-clusters|get-contexts|get-users}} --kubeconfig {{path/to/kubeconfig.yaml}}`

- Ստացեք ընթացիկ համատեքստը.:

`kubectl config current-context`

- Սահմանեք ընթացիկ համատեքստի լռելյայն անվանատարածքը.:

`kubectl config set-context --current --namespace {{namespace}}`

- Անցում այլ համատեքստի.:

`kubectl config {{[use|use-context]}} {{context_name}}`

- Ջնջել կլաստերները/համատեքստերը/օգտատերերը.:

`kubectl config {{delete-cluster|delete-context|delete-user}} {{cluster|context|user}}`

- Մշտապես ավելացրեք հատուկ kubeconfig ֆայլեր.:

`export KUBECONFIG="{{path/to/kubeconfig1.yaml}}:{{path/to/kubeconfig2.yaml}}"`
