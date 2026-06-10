# հարմարեցնել

> Հեշտությամբ տեղակայեք ռեսուրսներ Kubernetes-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kubernetes-sigs/kustomize/blob/master/site/content/en/docs/Reference/CLI/_index.md>:.

- Ստեղծեք kustomization ֆայլ ռեսուրսներով և անվանատարածքով.:

`kustomize create --resources {{deployment.yaml,service.yaml}} --namespace {{staging}}`

- Կառուցեք անհատականացման ֆայլ և տեղադրեք այն `kubectl`-ով:

`kustomize build . | kubectl apply {{[-f|--filename]}} -`

- Սահմանեք պատկերը kustomization ֆայլում.:

`kustomize edit set image {{busybox=alpine:3.6}}`

- Որոնեք Kubernetes ռեսուրսները ընթացիկ գրացուցակում, որոնք կավելացվեն kustomization ֆայլին.:

`kustomize create --autodetect`
