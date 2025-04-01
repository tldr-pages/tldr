# kubetail

> 用于同时跟踪多个 Kubernetes Pod 的日志的工具。
> 更多信息：<https://github.com/johanhaleby/kubetail>。

- 一次性跟踪多个 Pod（名称以 "my_app" 开头）的日志：

`kubetail {{my_app}}`

- 仅从多个 Pod 中跟踪特定的容器：

`kubetail {{my_app}} -c {{my_container}}`

- 从多个 Pod 中跟踪多个容器：

`kubetail {{my_app}} -c {{my_container_1}} -c {{my_container_2}}`

- 同时跟踪多个应用程序的日志，用逗号分隔：

`kubetail {{my_app_1}},{{my_app_2}}`
