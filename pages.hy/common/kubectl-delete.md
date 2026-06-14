# kubectl ջնջել

> Ջնջել Kubernetes ռեսուրսները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_delete/>:.

- Ջնջել կոնկրետ պատիճ.:

`kubectl delete {{[po|pods]}} {{pod_name}}`

- Ջնջել կոնկրետ տեղակայումը.:

`kubectl delete {{[deploy|deployments]}} {{deployment_name}}`

- Ջնջել կոնկրետ հանգույց.:

`kubectl delete {{[no|nodes]}} {{node_name}}`

- Ջնջել բոլոր պատյանները նշված անվանատարածքում.:

`kubectl delete {{[po|pods]}} --all {{[-n|--namespace]}} {{namespace}}`

- Ջնջել բոլոր տեղակայումները և ծառայությունները նշված անվանատարածքում.:

`kubectl delete {{[deploy|deployments]}},{{[svc|services]}} --all {{[-n|--namespace]}} {{namespace}}`

- Ջնջել բոլոր հանգույցները.:

`kubectl delete {{[no|nodes]}} --all`

- Ջնջել YAML մանիֆեստում սահմանված ռեսուրսները.:

`kubectl delete {{[-f|--filename]}} {{path/to/manifest.yaml}}`
