# go mod

> 模块维护。
> 更多信息：<https://golang.org/cmd/go/#hdr-Module_maintenance>。

- 在当前目录初始化新模块：

`go mod init {{moduleName}}`

- 下载模块到本地缓存：

`go mod download`

- 添加缺失的模块并移除未使用的模块：

`go mod tidy`

- 验证依赖项是否具有预期的内容：

`go mod verify`

- 将所有依赖项的源代码复制到 vendor 目录：

`go mod vendor`