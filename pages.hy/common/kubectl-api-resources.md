# kubectl api-ռեսուրսներ

> Տպեք աջակցվող API ռեսուրսները սերվերի վրա:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources/>:.

- Տպել աջակցվող API ռեսուրսները.:

`kubectl api-resources`

- Տպեք աջակցվող API ռեսուրսները լրացուցիչ տեղեկություններով.:

`kubectl api-resources {{[-o|--output]}} wide`

- Տպեք աջակցվող API ռեսուրսները՝ դասավորված ըստ սյունակի.:

`kubectl api-resources --sort-by {{name}}`

- Տպեք աջակցվող անվանատարածքային ռեսուրսները.:

`kubectl api-resources --namespaced`

- Տպեք աջակցվող ոչ անվանատարածքային ռեսուրսները.:

`kubectl api-resources --namespaced=false`

- Տպեք աջակցվող API ռեսուրսները որոշակի API խմբի հետ.:

`kubectl api-resources --api-group {{api_group}}`
