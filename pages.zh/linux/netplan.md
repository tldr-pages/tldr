# netplan

> 使用 YAML 的网络配置工具。
> 更多信息：<https://netplan.io/>。

- 应用网络配置并使其持久化：

`sudo netplan apply`

- 生成后端配置文件：

`sudo netplan generate`

- 配置网络接口使用 DHCP：

`sudo netplan set ethernets.{{interface_name}}.dhcp4=true`

- 尝试配置更改而不永久应用：

`sudo netplan try --timeout={{seconds}}`

- 在应用失败后恢复到之前的配置：

`sudo netplan --debug apply`

- 显示当前的 netplan 配置状态：

`netplan status`