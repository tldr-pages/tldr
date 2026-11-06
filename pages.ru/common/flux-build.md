# flux build

> Собирать манифесты Flux.
> Больше информации: <https://fluxcd.io/flux/cmd/flux_build/>.

- Собрать Kustomization:

`flux build kustomization {{имя}} --path {{путь/к/kustomization}}`

- Собрать Kustomization и сохранить манифесты в файл:

`flux build kustomization {{имя}} --path {{путь/к/kustomization}} >{{путь/к/manifests.yaml}}`

- Собрать Kustomization и передать результат напрямую в `kubectl`:

`flux build kustomization {{имя}} --path {{путь/к/kustomization}} | kubectl apply -f -`
