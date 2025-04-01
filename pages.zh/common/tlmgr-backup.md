# tlmgr backup

> 管理 TeX Live 包的备份。
> 默认备份目录由 `backupdir` 选项指定，可以通过 `tlmgr option` 获得。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 为一个或多个包创建备份：

`tlmgr backup {{package1 package2 ...}}`

- 为所有包创建备份：

`tlmgr backup --all`

- 将备份创建到自定义目录：

`tlmgr backup {{package}} --backupdir {{path/to/backup_directory}}`

- 删除一个或多个包的备份：

`tlmgr backup clean {{package1 package2 ...}}`

- 删除所有备份：

`tlmgr backup clean --all`