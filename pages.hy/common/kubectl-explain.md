# kubectl բացատրել

> Ցուցադրել Kubernetes API ռեսուրսի փաստաթղթերը, ներառյալ հասանելի դաշտերը և նկարագրությունները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_explain/>:.

- Ցույց տալ ռեսուրսի փաստաթղթերը.:

`kubectl explain {{pods|nodes|deployments|...}}`

- Ցուցադրել փաստաթղթերը օբյեկտի ենթառեսուրսի կամ դաշտի համար.:

`kubectl explain {{pod.spec.containers}}`

- Ցույց տալ փաստաթղթեր որոշակի տարբերակված ռեսուրսի համար.:

`kubectl explain {{ingress.v1.networking.k8s.io}}`

- Ցույց տալ բոլոր դաշտերը ռեկուրսիվորեն ռեսուրսի համար.:

`kubectl explain {{[po|pods]}} --recursive`

- Ցուցադրել օգնությունը.:

`kubectl explain --help`
