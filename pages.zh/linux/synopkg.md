# synopkg

> Synology DiskStation Manager 的软件包管理工具。
> 更多信息：<https://www.synology.com/dsm>。

- 列出已安装软件包的名称：

`synopkg list --name`

- 列出依赖于特定软件包的软件包：

`synopkg list --depend-on {{package}}`

- 启动/停止软件包：

`sudo synopkg {{start|stop}} {{package}}`

- 打印软件包的状态：

`synopkg status {{package}}`

- 卸载软件包：

`sudo synopkg uninstall {{package}}`

- 检查软件包是否有可用更新：

`synopkg checkupdate {{package}}`

- 将所有软件包升级到最新版本：

`sudo synopkg upgradeall`

- 从 synopkg 文件安装软件包：

`sudo synopkg install {{path/to/package.spk}}`