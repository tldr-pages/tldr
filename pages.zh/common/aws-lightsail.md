# aws lightsail

> 管理 Amazon Lightsail 资源。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html>.

- 列出所有虚拟私有服务器，或实例：

`aws lightsail get-instances`

- 列出所有套餐（实例计划）：

`aws lightsail list-bundles`

- 列出所有可用的实例镜像，或蓝图：

`aws lightsail list-blueprints`

- 创建一个实例：

`aws lightsail create-instances --instance-names {{name}} --availability-zone {{region}} --bundle-id {{nano_2_0}} --blueprint-id {{blueprint_id}}`

- 打印特定实例的状态：

`aws lightsail get-instance-state --instance-name {{name}}`

- 停止特定实例：

`aws lightsail stop-instance --instance-name {{name}}`

- 删除特定实例：

`aws lightsail delete-instance --instance-name {{name}}`
