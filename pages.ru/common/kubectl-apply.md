# kubectl apply

> Управлять приложениями через файлы, определяющие ресурсы Kubernetes.
> Создавать и обновлять ресурсы в кластере.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/>.

- Применить конфигурацию к ресурсу по имени файла:

`kubectl apply {{[-f|--filename]}} {{путь/к/файлу}}`

- Применить конфигурацию к ресурсу из `kustomization.yaml` в каталоге:

`kubectl apply {{[-k|--kustomize]}} {{путь/к/каталогу}}`

- Применить конфигурацию к ресурсу через `stdin`:

`{{cat pod.json}} | kubectl apply {{[-f|--filename]}} -`

- Отредактировать последние аннотации last-applied-configuration ресурсов в редакторе по умолчанию:

`kubectl apply edit-last-applied {{[-f|--filename]}} {{путь/к/файлу}}`

- Установить последние аннотации last-applied-configuration в соответствии с содержимым файла:

`kubectl apply set-last-applied {{[-f|--filename]}} {{путь/к/файлу}}`

- Просмотреть последние аннотации last-applied-configuration по типу/имени или файлу:

`kubectl apply view-last-applied {{[-f|--filename]}} {{путь/к/файлу}}`
