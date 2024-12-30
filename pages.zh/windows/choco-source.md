# choco 源

> 管理 Chocolatey 的软件包源。
> 更多信息：<https://chocolatey.org/docs/commands/source>。

- 列出当前可用的源：

`choco source list`

- 添加一个新的软件包源：

`choco source add --name {{name}} --source {{url}}`

- 添加一个带有凭据的新软件包源：

`choco source add --name {{name}} --source {{url}} --user {{username}} --password {{password}}`

- 添加一个带有客户端证书的新软件包源：

`choco source add --name {{name}} --source {{url}} --cert {{path\to\certificate_file}}`

- 启用一个软件包源：

`choco source enable --name {{name}}`

- 禁用一个软件包源：

`choco source disable --name {{name}}`

- 移除一个软件包源：

`choco source remove --name {{name}}`