# mokutil

> 配置安全启动所有者密钥（MOK）。
> 某些操作，如启用和禁用安全启动或注册密钥，可能需要重新启动。
> 更多信息：<https://github.com/lcp/mokutil>。

- 显示安全启动是否已启用：

`mokutil --sb-state`

- 启用安全启动：

`mokutil --enable-validation`

- 禁用安全启动：

`mokutil --disable-validation`

- 列出已注册的密钥：

`mokutil --list-enrolled`

- 注册新的密钥：

`mokutil --import {{path/to/key.der}}`

- 列出待注册的密钥：

`mokutil --list-new`

- 设置 shim 的详细程度：

`mokutil --set-verbosity true`
