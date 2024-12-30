# apk

> Alpine Linux 包管理工具。
> 更多信息：<https://manned.org/apk>。

- 从所有远程仓库更新软件包索引：

`apk update`

- 安装一个新软件包：

`apk add {{package}}`

- 删除一个软件包：

`apk del {{package}}`

- 修复一个软件包或在不修改主要依赖项的情况下升级它：

`apk fix {{package}}`

- 通过关键字搜索软件包：

`apk search {{keywords}}`

- 显示特定软件包的信息：

`apk info {{package}}`