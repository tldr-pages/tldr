# tlmgr 恢复

> 恢复使用 `tlmgr backup` 创建的包备份。
> 默认的备份目录由 `backupdir` 选项指定，可以通过 `tlmgr option` 获取。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出所有包的所有可用备份版本：

`tlmgr restore`

- 列出特定包的所有可用备份版本：

`tlmgr restore {{package}}`

- 恢复特定包的特定版本：

`tlmgr restore {{package}} {{revision}}`

- 恢复所有备份包的最新版本：

`tlmgr restore --all`

- 从自定义备份目录恢复一个包：

`tlmgr restore {{package}} {{revision}} --backupdir {{path/to/backup_directory}}`

- 执行干运行并打印所有操作而不执行它们：

`tlmgr restore --dry-run {{package}} {{revision}}`