# apk

> Alpine linux的包管理工具.

- 从所有的远程仓库中更新仓库索引:

`apk update`

- 安装一个新软件包:

`apk add {{package}}`

- 移除一个软件包:

`apk del {{package}}`

- 修复或更新软件包而不修改主依赖项:

`apk fix {{package}}`

- 通过关键字查找软件包:

`apk search {{keyword}}`

- 获取指定软件包的相关信息:

`apk info {{package}}`
