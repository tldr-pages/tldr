# port

> macOS 包管理器软件（类似 brew）。
> 更多信息：<https://www.macports.org>.

- 搜索包：

`port search {{搜索的包名}}`

- 安装软件包：

`sudo port install {{报名}}`

- 列出已安装的软件包：

`port installed`

- 更新 port 自身，并获取可用包的最新列表：

`sudo port selfupdate`

- 升级过时的软件包：

`sudo port upgrade outdated`

- 删除已安装的软件包的旧版本：

`sudo port uninstall inactive`
