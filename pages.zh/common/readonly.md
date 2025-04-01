# readonly

> 设置只读的 shell 变量。
> 更多信息：<https://manned.org/readonly.1posix>.

- 设置一个只读变量：

`readonly {{variable_name}}={{value}}`

- 标记一个变量为只读：

`readonly {{existing_variable}}`

- [p]rint 打印所有只读变量的名称和值到 `stdout`：

`readonly -p`