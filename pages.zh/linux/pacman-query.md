# pacman --query

> Arch Linux 包管理工具。
> 另见：`pacman`。
> 更多信息：<https://manned.org/pacman.8>。

- [Q] 查询本地软件包数据库并列出已安装的软件包及其版本：

`pacman -Q`

- 仅列出被 [e] 明确安装的软件包及其版本：

`pacman -Qe`

- 查找哪个软件包 [o] 拥有一个文件：

`pacman -Qo {{filename}}`

- 显示有关已安装软件包的 [i] 信息：

`pacman -Qi {{package}}`

- 显示特定软件包拥有的文件 [l] 列表：

`pacman -Ql {{package}}`

- 列出孤立的软件包（作为 [d] 依赖安装但未被任何软件包所需的 ([t])），并以 [q] 静默模式输出（仅显示软件包名称）：

`pacman -Qdtq`

- 列出来自仓库数据库的已安装外部软件包 ([m])：

`pacman -Qm`

- 列出可以 [u] 升级的软件包：

`pacman -Qu`