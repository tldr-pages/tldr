# pkg_info

> 查看 OpenBSD 中的包信息。
> 参见：`pkg_add`，`pkg_delete`。
> 更多信息：<https://man.openbsd.org/pkg_info>。

- 使用包名称搜索包：

`pkg_info -Q {{package}}`

- 输出已安装包的列表，以便与 `pkg_add -l` 一起使用：

`pkg_info -mz`