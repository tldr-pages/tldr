# helm

> Kubernetes 的包管理器。
> 一些子命令（如 `install`）有它们自己的使用文档。
> 更多信息：<https://helm.sh/>。

- 创建一个 Helm Chart：

`helm create {{chart_name}}`

- 添加一个新的 Helm 仓库：

`helm repo add {{repository_name}}`

- 列出 Helm 仓库：

`helm repo list`

- 更新 Helm 仓库：

`helm repo update`

- 删除一个 Helm 仓库：

`helm repo remove {{repository_name}}`

- 安装一个 Helm Chart：

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- 下载 Helm Chart 作为 tar 归档文件：

`helm get {{chart_release_name}}`

- 更新 Helm 依赖：

`helm dependency update`