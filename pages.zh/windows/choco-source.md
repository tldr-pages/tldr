# choco source

> 使用 Chocolatey 管理包的源。
> 更多信息：<https://chocolatey.org/docs/commands-source>.

- 列出当前可用的源：

`choco source list`

- 添加一个新的包源：

`choco source add --name {{名称}} --source {{url}}`

- 添加包含凭据的新包源：

`choco source add --name {{名称}} --source {{url}} --user {{用户名}} --password {{密码}}`

- 使用客户端证书添加新的包源：

`choco source add --name {{名称}} --source {{url}} --cert {{证书的路径}}`

- 启用一个包源：

`choco source enable --name {{名称}}`

- 禁用一个包源：

`choco source disable --name {{名称}}`

- 移除一个包源：

`choco source remove --name {{名称}}`
