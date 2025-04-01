# dep

> 部署 PHP 应用程序。
> 注意：同名的 Go 命令 `dep` 已被弃用并归档。
> 更多信息：<https://deployer.org>.

- 以交互方式在本地路径初始化部署器（使用框架模板时使用 `--template=模板`）：

`dep init`

- 将应用程序部署到远程主机：

`dep deploy {{hostname}}`

- 回滚到上一个有效的版本：

`dep rollback`

- 通过 SSH 连接到远程主机：

`dep ssh {{hostname}}`

- 列出命令：

`dep list`

- 在远程主机上运行任意命令：

`dep run "{{command}}"`

- 显示命令的帮助信息：

`dep help {{command}}`
