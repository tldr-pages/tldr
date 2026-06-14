# kubectl auth

> Ստուգեք մուտքի թույլտվությունները Kubernetes կլաստերում:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/>:.

- Ստուգեք, արդյոք ներկայիս օգտվողը կարող է կատարել բոլոր գործողությունները բոլոր ռեսուրսների վրա որոշակի անվանատարածքում.:

`kubectl auth can-i '*' '*' {{[-n|--namespace]}} {{namespace}}`

- Ստուգեք, արդյոք ներկայիս օգտվողը կարող է կատարել կոնկրետ բայ որոշակի ռեսուրսի վրա.:

`kubectl auth can-i {{verb}} {{resource}} {{[-n|--namespace]}} {{namespace}}`

- Ստուգեք, արդյոք որոշակի օգտվողի կամ ծառայության հաշիվը կարող է որևէ գործողություն կատարել ռեսուրսի վրա.:

`kubectl auth can-i {{verb}} {{resource}} {{[-n|--namespace]}} {{namespace}} --as {{user_or_sa}}`

- Թվարկեք բոլոր գործողությունները, որոնք ներկայիս օգտվողին թույլատրվում է կատարել անունների տարածքում.:

`kubectl auth can-i --list {{[-n|--namespace]}} {{namespace}}`
