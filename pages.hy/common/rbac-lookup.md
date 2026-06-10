# rbac-որոնում

> Գտեք դերեր և կլաստերի դերեր, որոնք կցված են ցանկացած օգտվողի, ծառայության հաշվին կամ խմբի անվանմանը ձեր Kubernetes կլաստերում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/FairwindsOps/rbac-lookup>:.

- Դիտեք բոլոր RBAC կապերը.:

`rbac-lookup`

- Դիտեք RBAC կապերը, որոնք համապատասխանում են տվյալ արտահայտությանը.:

`rbac-lookup {{search_term}}`

- Դիտեք բոլոր RBAC կապերը աղբյուրի դերի հետ միասին.:

`rbac-lookup {{[-o|--output]}} wide`

- Դիտեք բոլոր RBAC կապերը՝ զտված ըստ թեմայի.:

`rbac-lookup {{[-k|--kind]}} {{user|group|serviceaccount}}`

- Դիտեք բոլոր RBAC կապերը IAM դերերի հետ միասին (եթե օգտագործում եք GKE):

`rbac-lookup --gke`
