# gcloud 配置

> 管理 `gcloud` 的不同配置。
> 另见：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/config>。

- 为当前配置定义一个属性（如 compute/zone）：

`gcloud config set {{property}} {{value}}`

- 获取 `gcloud` 属性的值：

`gcloud config get {{property}}`

- 显示当前配置的所有属性：

`gcloud config list`

- 创建一个具有给定名称的新配置：

`gcloud config configurations create {{configuration_name}}`

- 显示所有可用配置的列表：

`gcloud config configurations list`

- 切换到具有给定名称的现有配置：

`gcloud config configurations activate {{configuration_name}}`