# pacman --query

> Arch Linux 包管理工具。
> 详见: `pacman`。
> 更多信息: <https://manned.org/pacman.8>。

- [Q]查询本地包数据库并列出已安装的包及其版本：

`pacman -Q`

- 仅列出明确安装的包及其版本：

`pacman -Qe`

- 查找拥有某文件的包：

`pacman -Qo {{filename}}`

- 显示已安装包的详细信息：

`pacman -Qi {{package}}`

- 显示特定包包含的文件列表：

`pacman -Ql {{package}}`

- 列出孤儿包（作为依赖安装但不再被任何包需要([t])，并以[q]安静模式显示（仅显示包名））：

`pacman -Qdtq`

- 列出不在仓库数据库中的外来包([m])：

`pacman -Qm`

- 列出可以升级的包：

`pacman -Qu`