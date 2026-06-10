# kubectl վերև

> Տեսեք ռեսուրսների սպառումը հանգույցների կամ պատյանների համար:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top/>:.

- Ստացեք բոլոր հանգույցների ռեսուրսների սպառումը.:

`kubectl top {{[no|nodes]}}`

- Ստացեք որոշակի հանգույցի ռեսուրսների սպառումը.:

`kubectl top {{[no|nodes]}} {{node_name}}`

- Ստացեք բոլոր պատյանների ռեսուրսների սպառումը.:

`kubectl top {{[po|pods]}}`

- Ստացեք որոշակի պատի ռեսուրսների սպառումը.:

`kubectl top {{[po|pods]}} {{pod_name}}`

- Ստացեք ռեսուրսների սպառումը բոլոր պատյանների անվանական տարածքում.:

`kubectl top {{[po|pods]}} {{[-n|--namespace]}} {{namespace_name}}`

- Ստացեք բոլոր բեռնարկղերի ռեսուրսների սպառումը պատիճում.:

`kubectl top {{[po|pods]}} --containers`

- Ստացեք բոլոր պատյանների ռեսուրսների սպառումը նշված պիտակով.:

`kubectl top {{[po|pods]}} {{[-l|--selector]}} {{key=value}}`
