# aws lightsail

> 管理 Amazon Lightsail 资源。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/lightsail/>.

- 列出所有虚拟专用服务器（或实例）：

`aws lightsail get-instances`

- 列出所有套餐（实例计划）：

`aws lightsail list-bundles`

- 列出所有可用的实例镜像（或蓝图）：

`aws lightsail list-blueprints`

- 创建一个实例：

`aws lightsail create-instances --instance-names {{名称}} --availability-zone {{区域}} --bundle-id {{nano_2_0}} --blueprint-id {{蓝图_id}}`

- 输出指定实例的状态：

`aws lightsail get-instance-state --instance-name {{名称}}`

- 停止指定实例：

`aws lightsail stop-instance --instance-name {{名称}}`

- 删除指定实例：

`aws lightsail delete-instance --instance-name {{名称}}`
