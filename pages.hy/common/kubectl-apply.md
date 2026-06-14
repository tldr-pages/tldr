# kubectl դիմել

> Կառավարեք հավելվածները Kubernetes-ի ռեսուրսները սահմանող ֆայլերի միջոցով:.
> Ստեղծեք և թարմացրեք ռեսուրսները կլաստերում:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/>:.

- Կիրառեք կոնֆիգուրացիա ռեսուրսի վրա՝ ըստ ֆայլի անունով.:

`kubectl apply {{[-f|--filename]}} {{path/to/file}}`

- Կիրառեք կոնֆիգուրացիան ռեսուրսին `kustomization.yaml`-ից գրացուցակում.:

`kubectl apply {{[-k|--kustomize]}} {{path/to/directory}}`

- Կիրառեք կոնֆիգուրացիան ռեսուրսի վրա `stdin`-ով.:

`{{cat pod.json}} | kubectl apply {{[-f|--filename]}} -`

- Խմբագրել ռեսուրսների վերջին կիրառված կոնֆիգուրացիայի վերջին անոտացիաները լռելյայն խմբագրիչից.:

`kubectl apply edit-last-applied {{[-f|--filename]}} {{path/to/file}}`

- Սահմանեք վերջին կիրառված կոնֆիգուրացիայի անոտացիաները՝ սահմանելով այն համապատասխանեցնելով ֆայլի բովանդակությանը.:

`kubectl apply set-last-applied {{[-f|--filename]}} {{path/to/file}}`

- Դիտեք վերջին կիրառված կազմաձևման ծանոթագրությունները ըստ տեսակի/անունի կամ ֆայլի.:

`kubectl apply view-last-applied {{[-f|--filename]}} {{path/to/file}}`
