# kubectl ստանալ

> Ստացեք Kubernetes օբյեկտներ և ռեսուրսներ:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/>:.

- Ստացեք բոլոր անվանատարածքները ընթացիկ կլաստերի մեջ.:

`kubectl get {{[ns|namespaces]}}`

- Ստացեք հանգույցներ նշված անվանատարածքում.:

`kubectl get {{[no|nodes]}} {{[-n|--namespace]}} {{namespace}}`

- Ստացեք պատյաններ նշված անվանատարածքում.:

`kubectl get {{[po|pods]}} {{[-n|--namespace]}} {{namespace}}`

- Ստացեք տեղակայումներ նշված անվանատարածքում.:

`kubectl get {{[deploy|deployments]}} {{[-n|--namespace]}} {{namespace}}`

- Ստացեք ծառայություններ նշված անվանատարածքում.:

`kubectl get {{[svc|services]}} {{[-n|--namespace]}} {{namespace}}`

- Ստացեք այլ ռեսուրսներ.:

`kubectl get {{persistentvolumeclaims|secret|...}}`

- Ստացեք բոլոր ռեսուրսները բոլոր անվանատարածքներում.:

`kubectl get all {{[-A|--all-namespaces]}}`

- Ստացեք Kubernetes օբյեկտները, որոնք սահմանված են YAML մանիֆեստի ֆայլում.:

`kubectl get {{[-f|--filename]}} {{path/to/manifest.yaml}}`
