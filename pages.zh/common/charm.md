# charm

> 一套工具，可为您的基于终端的应用程序添加后端，无需担心用户帐户、数据存储和加密。
> 更多信息：<https://github.com/charmbracelet/charm>.

- 备份您的 Charm 帐户密钥：

`charm backup-keys`

- 将 Charm 帐户密钥备份到特定位置：

`charm backup-keys -o {{path/to/output_file.tar}}`

- 导入之前备份的 Charm 帐户密钥：

`charm import-keys "{{charm-keys-backup.tar}}"`

- 查找 `cloud.charm.sh` 文件夹在您计算机上的位置：

`charm where`

- 启动您的 Charm 服务器：

`charm serve`

- 打印链接的 SSH 密钥：

`charm keys`

- 打印您的 Charm ID：

`charm id`
