# gcloud config

> 管理 `gcloud` 的不同配置。
> 查看更多：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/config>。

- 为当前配置定义一个属性（如 compute/zone）：

`gcloud config set {{property}} {{value}}`

- 获取 `gcloud` 属性的值：

`gcloud config get {{property}}`

- 显示当前配置的所有属性：

`gcloud config list`

- 使用给定的名称创建一个新的配置：

`gcloud config configurations create {{configuration_name}}`

- 显示所有可用配置的列表：

`gcloud config configurations list`

- 切换到具有给定名称的现有配置：

`gcloud config configurations activate {{configuration_name}}`
