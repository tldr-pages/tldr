# alien

> 将不同的安装包转换为其他格式。
> 另请参见：`debtap`，用于在 Arch Linux 上进行 `.deb` 转换。
> 更多信息：<https://manned.org/alien>。

- 将特定的安装文件转换为 Debian 格式（`.deb` 扩展名）：

`sudo alien --to-deb {{path/to/file}}`

- 将特定的安装文件转换为 Red Hat 格式（`.rpm` 扩展名）：

`sudo alien --to-rpm {{path/to/file}}`

- 将特定的安装文件转换为 Slackware 安装文件（`.tgz` 扩展名）：

`sudo alien --to-tgz {{path/to/file}}`

- 将特定的安装文件转换为 Debian 格式并安装到系统中：

`sudo alien --to-deb --install {{path/to/file}}`