#ղեկ

> Փաթեթի կառավարիչ Kubernetes-ի համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `install`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://helm.sh/docs/helm/>:.

- Ստեղծեք ղեկային աղյուսակ.:

`helm create {{chart_name}}`

- Ավելացնել նոր ղեկի պահոց.:

`helm repo add {{repository_name}}`

- Ցուցակեք ղեկի պահոցները.:

`helm repo {{[ls|list]}}`

- Թարմացրեք ղեկի պահոցները.:

`helm repo {{[up|update]}}`

- Ջնջել ղեկի պահոցը.:

`helm repo {{[rm|remove]}} {{repository_name}}`

- Տեղադրեք ղեկի աղյուսակը.:

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- Ներբեռնեք ղեկային աղյուսակը որպես `.tar` արխիվ.:

`helm get {{chart_release_name}}`

- Թարմացրեք ղեկի կախվածությունները.:

`helm {{[dep|dependency]}} {{[up|update]}}`
