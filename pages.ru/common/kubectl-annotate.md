# kubectl annotate

> Аннотировать ресурсы Kubernetes.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/>.

- Добавить аннотацию к поду:

`kubectl annotate {{[po|pods]}} {{имя_пода}} {{ключ}}={{значение}}`

- Обновить аннотацию пода, перезаписав существующее значение:

`kubectl annotate {{[po|pods]}} {{имя_пода}} {{ключ}}={{значение}} --overwrite`

- Добавить аннотацию ко всем подам в пространстве имён с определённым селектором меток:

`kubectl annotate {{[po|pods]}} {{ключ}}={{значение}} {{[-l|--selector]}} {{ключ_метки}}={{значение_метки}}`

- Вывести список всех аннотаций пода:

`kubectl annotate {{[po|pods]}} {{имя_пода}} --list`

- Удалить аннотацию с пода:

`kubectl annotate {{[po|pods]}} {{имя_пода}} {{ключ}}-`
