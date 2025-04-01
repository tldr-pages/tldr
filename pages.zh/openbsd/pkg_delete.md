# pkg_delete

> 在 OpenBSD 中移除软件包。
> 参见：`pkg_add`，`pkg_info`。
> 更多信息：<https://man.openbsd.org/pkg_delete>。

- 删除一个软件包：

`pkg_delete {{package}}`

- 删除一个软件包，包括其未使用的依赖项：

`pkg_delete -a {{package}}`

- 模拟删除一个软件包（不实际执行删除）：

`pkg_delete -n {{package}}`
