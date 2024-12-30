# synopkg

> 用于Synology DiskStation Manager的包管理工具。
> 更多信息：<https://www.synology.com/dsm>。

- 列出已安装包的名称：

`synopkg list --name`

- 列出依赖于特定包的包：

`synopkg list --depend-on {{package}}`

- 启动/停止一个包：

`sudo synopkg {{start|stop}} {{package}}`

- 打印包的状态：

`synopkg status {{package}}`

- 卸载一个包：

`sudo synopkg uninstall {{package}}`

- 检查包是否有可用更新：

`synopkg checkupdate {{package}}`

- 升级所有包到最新版本：

`sudo synopkg upgradeall`

- 从synopkg文件安装包：

`sudo synopkg install {{path/to/package.spk}}`