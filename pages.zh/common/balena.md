# balena

> 与 balenaCloud、openBalena 和 balena API 交互。
> 更多信息：<https://www.balena.io/docs/reference/cli/>.

- 登录 balenaCloud 账户：

`balena login`

- 创建 balenaCloud 或 openBalena 应用：

`balena app create {{app_name}}`

- 列出账户中所有的 balenaCloud 或 openBalena 应用：

`balena apps`

- 列出与 balenaCloud 或 openBalena 账户关联的所有设备：

`balena devices`

- 将 balenaOS 镜像刷写到本地磁盘：

`balena local flash {{path/to/balenaos.img}} --drive {{drive_location}}`
