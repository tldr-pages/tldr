# kubectl խմբագրում

> Խմբագրել Kubernetes-ի ռեսուրսները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit/>:.

- Խմբագրել պատիճը լռելյայն անվանատարածքում.:

`kubectl edit {{[po|pods]}}/{{pod_name}}`

- Խմբագրել տեղակայումը լռելյայն անվանատարածքում.:

`kubectl edit {{[deploy|deployment]}}/{{deployment_name}}`

- Խմբագրել ծառայությունը լռելյայն անվանատարածքում.:

`kubectl edit {{[svc|service]}}/{{service_name}}`

- Խմբագրել տվյալ ռեսուրսի բոլոր գրառումները տվյալ անվանատարածքում.:

`kubectl edit {{resource}} {{[-n|--namespace]}} {{namespace}}`

- Խմբագրել ռեսուրսը հատուկ խմբագրիչի միջոցով.:

`KUBE_EDITOR={{nano}} kubectl edit {{resource}}/{{resource_name}}`

- Խմբագրել ռեսուրսը JSON ձևաչափով.:

`kubectl edit {{resource}}/{{resource_name}} {{[-o|--output]}} json`
