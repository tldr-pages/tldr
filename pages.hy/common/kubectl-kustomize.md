# kubectl kustomize

> Կառուցեք Kubernetes ռեսուրսների մի շարք՝ օգտագործելով `kustomization.yaml` ֆայլը:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kustomize/>:.

- Ստեղծեք ռեսուրսներ ընթացիկ գրացուցակից.:

`kubectl kustomize`

- Ստեղծեք ռեսուրսներ որոշակի գրացուցակից.:

`kubectl kustomize {{path/to/directory}}`

- Ստեղծեք ռեսուրսներ հեռավոր URL-ից.:

`kubectl kustomize {{https://github.com/user/repo/path}}`

- Ստեղծեք ռեսուրսներ և պահեք ֆայլում.:

`kubectl kustomize {{path/to/directory}} > {{output.yaml}}`

- Ստեղծեք ռեսուրսներ՝ անջատված բեռի սահմանափակիչով.:

`kubectl kustomize --load-restrictor {{LoadRestrictionsNone}} {{path/to/directory}}`
