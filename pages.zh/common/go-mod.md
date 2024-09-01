# go mod

> 模块维护。
> 更多信息：<https://golang.org/cmd/go/#hdr-Module_maintenance>.

- 在当前目录初始化新模块：

`go mod init {{模块名}}`

- 下载模块到本地缓存：

`go mod download`

- 添加缺失的模块并删除无用的模块：

`go mod tidy`

- 验证依赖项是否具有预期内容：

`go mod verify`

- 复制所有依赖的源码到 vendor 目录：

`go mod vendor`
