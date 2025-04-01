# tlmgr restore

> 恢复使用 `tlmgr backup` 创建的软件包备份。
> 默认备份目录由 `backupdir` 选项指定，可以通过 `tlmgr option` 获取。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>.

- 列出所有软件包的所有可用备份版本：

`tlmgr restore`

- 列出特定软件包的所有可用备份版本：

`tlmgr restore {{package}}`

- 恢复特定软件包的特定版本：

`tlmgr restore {{package}} {{revision}}`

- 恢复所有备份软件包的最新版本：

`tlmgr restore --all`

- 从自定义备份目录恢复软件包：

`tlmgr restore {{package}} {{revision}} --backupdir {{path/to/backup_directory}}`

- 执行预演并打印所有将要采取的操作，但不实际执行：

`tlmgr restore --dry-run {{package}} {{revision}}`
