# apk

> Alpine Linux 的包管理工具。
> 更多信息：<https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- 从所有的远程仓库中更新仓库索引：

`apk update`

- 安装一个新软件包：

`apk add {{软件包}}`

- 移除一个软件包：

`apk del {{软件包}}`

- 修复或更新软件包而不修改主依赖项：

`apk fix {{软件包}}`

- 通过关键字查找软件包：

`apk search {{关键字}}`

- 获取指定软件包的相关信息：

`apk info {{软件包}}`
