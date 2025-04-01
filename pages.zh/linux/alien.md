# alien

> 转换不同的安装包为其他格式。
> 另请参阅：`debtap`，用于在 Arch Linux 上转换 `.deb` 包。
> 更多信息：<https://manned.org/alien>.

- 将特定安装文件转换为 Debian 格式（扩展名为 `.deb`）：

`sudo alien --to-deb {{path/to/file}}`

- 将特定安装文件转换为 Red Hat 格式（扩展名为 `.rpm`）：

`sudo alien --to-rpm {{path/to/file}}`

- 将特定安装文件转换为 Slackware 安装文件（扩展名为 `.tgz`）：

`sudo alien --to-tgz {{path/to/file}}`

- 将特定安装文件转换为 Debian 格式并安装到系统中：

`sudo alien --to-deb --install {{path/to/file}}`