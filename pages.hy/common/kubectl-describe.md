# kubectl նկարագրել

> Ցույց տալ Kubernetes-ի ռեսուրսների մանրամասները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/>:.

- Ցույց տալ պատիճների մանրամասները անունների տարածքում.:

`kubectl describe {{[po|pods]}} {{[-n|--namespace]}} {{namespace}}`

- Ցույց տալ հանգույցների մանրամասները անունների տարածքում.:

`kubectl describe {{[no|nodes]}} {{[-n|--namespace]}} {{namespace}}`

- Ցույց տալ կոնկրետ պատի մանրամասները անվանատարածքում.:

`kubectl describe {{[po|pods]}} {{pod_name}} {{[-n|--namespace]}} {{namespace}}`

- Ցույց տալ կոնկրետ հանգույցի մանրամասները անվանատարածքում.:

`kubectl describe {{[no|nodes]}} {{node_name}} {{[-n|--namespace]}} {{namespace}}`

- Ցույց տալ YAML մանիֆեստի ֆայլում սահմանված Kubernetes օբյեկտների մանրամասները.:

`kubectl describe {{[-f|--filename]}} {{path/to/manifest.yaml}}`
