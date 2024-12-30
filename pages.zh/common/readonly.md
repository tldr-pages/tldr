# 只读

> 设置只读的 shell 变量。
> 更多信息：<https://manned.org/readonly.1posix>。

- 设置一个只读变量：

`readonly {{变量名}}={{值}}`

- 将一个变量标记为只读：

`readonly {{已有变量}}`

- [p]rint 所有只读变量的名称和值到 `stdout`：

`readonly -p`