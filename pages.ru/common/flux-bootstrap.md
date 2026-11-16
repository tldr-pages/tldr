# flux bootstrap

> Выполнять начальную установку Flux в кластере Kubernetes.
> Больше информации: <https://fluxcd.io/flux/cmd/flux_bootstrap/>.

- Выполнить начальную установку с использованием репозитория GitHub:

`flux bootstrap github --owner {{owner}} --repository {{repository}} --path {{путь/к/каталогу_кластера}} --personal`

- Выполнить начальную установку с использованием репозитория GitLab:

`flux bootstrap gitlab --owner {{owner}} --repository {{repository}} --path {{путь/к/каталогу_кластера}}`

- Выполнить начальную установку из произвольного Git-репозитория через SSH:

`flux bootstrap git --url {{ssh://git@example.com/repository.git}} --branch {{main}} --path {{путь/к/каталогу_кластера}}`
