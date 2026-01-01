# choco source

> 使用 Chocolatey 管理包的源。
> 更多信息：<https://docs.chocolatey.org/en-us/choco/commands/source/>。

- 列出当前可用的源：

`choco source list`

- 添加一个新的包源：

`choco source add {{[-n|--name]}} {{名称}} {{[-s|--source]}} {{url}}`

- 添加包含凭据的新包源：

`choco source add {{[-n|--name]}} {{名称}} {{[-s|--source]}} {{url}} {{[-u|--user]}} {{用户名}} {{[-p|--password]}} {{密码}}`

- 使用客户端证书添加新的包源：

`choco source add {{[-n|--name]}} {{名称}} {{[-s|--source]}} {{url}} --cert {{证书的路径}}`

- 启用一个包源：

`choco source enable {{[-n|--name]}} {{名称}}`

- 禁用一个包源：

`choco source disable {{[-n|--name]}} {{名称}}`

- 移除一个包源：

`choco source remove {{[-n|--name]}} {{名称}}`
