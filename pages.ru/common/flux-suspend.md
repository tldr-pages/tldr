# flux suspend

> Приостанавливать ресурсы Flux.
> Больше информации: <https://fluxcd.io/flux/cmd/flux_suspend/>.

- Приостановить согласование для Kustomization:

`flux suspend kustomization {{имя_kustomization}}`

- Приостановить согласование для всех Kustomization в пространстве имён:

`flux suspend kustomization --all`

- Приостановить согласование для HelmRelease:

`flux suspend helmrelease {{имя_релиза}}`

- Приостановить согласование для источника GitRepository:

`flux suspend source git {{имя_источника}}`

- Приостановить согласование для ресурса ImageUpdateAutomation:

`flux suspend image update {{имя_автоматизации}}`
