# kubetail

> 同时跟踪多个Kubernetes pod的日志的工具。
> 更多信息：<https://github.com/johanhaleby/kubetail>。

- 一次性跟踪多个名称以“my_app”开头的pod的日志：

`kubetail {{my_app}}`

- 仅跟踪多个pod中的特定容器：

`kubetail {{my_app}} -c {{my_container}}`

- 从多个pod中跟踪多个容器：

`kubetail {{my_app}} -c {{my_container_1}} -c {{my_container_2}}`

- 同时跟踪多个应用程序，用逗号分隔：

`kubetail {{my_app_1}},{{my_app_2}}`