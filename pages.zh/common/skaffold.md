# skaffold

> 促进 Kubernetes 应用程序的持续开发。
> 更多信息：<https://skaffold.dev>。

- 构建工件：

`skaffold build -f {{skaffold.yaml}}`

- 每次代码更改时构建并部署您的应用：

`skaffold dev -f {{skaffold.yaml}}`

- 运行管道文件：

`skaffold run -f {{skaffold.yaml}}`

- 对 Skaffold 进行诊断：

`skaffold diagnose -f {{skaffold.yaml}}`

- 部署工件：

`skaffold deploy -f {{skaffold.yaml}}`