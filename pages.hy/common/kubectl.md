# կուբեկտլ

> Գործարկել հրամաններ Kubernetes կլաստերների դեմ:.
> Որոշ ենթահրամաններ, ինչպիսիք են `run`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/>:.

- Թվարկեք տեղեկատվություն ռեսուրսի մասին ավելի մանրամասն.:

`kubectl get {{pods|service|deployment|ingress|...}} {{[-o|--output]}} wide`

- Թարմացրեք նշված pod `unhealthy` պիտակով և `true` արժեքով:

`kubectl label pods {{name}} unhealthy=true`

- Թվարկեք բոլոր ռեսուրսները տարբեր տեսակներով.:

`kubectl get all`

- Ցուցադրել հանգույցների կամ պատյանների ռեսուրսի (CPU/Հիշողություն/Պահպանում) օգտագործումը.:

`kubectl top {{pods|nodes}}`

- Տպեք հիմնական և կլաստերային ծառայությունների հասցեն.:

`kubectl cluster-info`

- Ցուցադրել կոնկրետ դաշտի բացատրությունը.:

`kubectl explain {{pods.spec.containers}}`

- Տպեք տեղեկամատյանները կոնտեյների համար պատյանում կամ նշված ռեսուրսում.:

`kubectl logs {{pod_name}}`

- Գործարկեք հրամանը գոյություն ունեցող պատիճում.:

`kubectl exec {{pod_name}} -- {{ls /}}`
