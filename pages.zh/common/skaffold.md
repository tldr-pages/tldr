# skaffold

> 为 Kubernetes 应用程序提供持续开发支持。
> 更多信息：<https://skaffold.dev>。

- 构建制品：

`skaffold build -f {{skaffold.yaml}}`

- 每当代码更改时构建并部署应用：

`skaffold dev -f {{skaffold.yaml}}`

- 运行管道文件：

`skaffold run -f {{skaffold.yaml}}`

- 对 Skaffold 进行诊断：

`skaffold diagnose -f {{skaffold.yaml}}`

- 部署制品：

`skaffold deploy -f {{skaffold.yaml}}`