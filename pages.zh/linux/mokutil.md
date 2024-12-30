# mokutil

> 配置安全启动机器所有者密钥 (MOK)。
> 一些操作，如启用和禁用安全启动或注册密钥，需要重启。
> 更多信息：<https://github.com/lcp/mokutil>。

- 显示安全启动是否启用：

`mokutil --sb-state`

- 启用安全启动：

`mokutil --enable-validation`

- 禁用安全启动：

`mokutil --disable-validation`

- 列出注册的密钥：

`mokutil --list-enrolled`

- 注册一个新密钥：

`mokutil --import {{path/to/key.der}}`

- 列出待注册的密钥：

`mokutil --list-new`

- 设置 shim 详细级别：

`mokutil --set-verbosity true`