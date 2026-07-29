# balena

> 与 balenaCloud、openBalena 和 balena API 交互。
> 更多信息：<https://docs.balena.io/reference/balena-cli/latest/>。

- 登录 balenaCloud 账户：

`balena login`

- 创建 balenaCloud 或 openBalena 应用程序：

`balena app create {{应用程序名称}}`

- 列出账户中所有 balenaCloud 或 openBalena 应用程序：

`balena apps`

- 列出与 balenaCloud 或 openBalena 账户关联的所有设备：

`balena devices`

- 将 balenaOS 镜像刷入本地驱动器：

`balena local flash {{路径/到/balenaos.img}} --drive {{驱动器位置}}`
