# pkg_add

> 在OpenBSD中安装/更新软件包。
> 另见: `pkg_info`, `pkg_delete`。
> 更多信息: <https://man.openbsd.org/pkg_add>。

- 更新所有软件包，包括依赖项：

`pkg_add -u`

- 安装一个新软件包：

`pkg_add {{package}}`

- 从`pkg_info`的原始输出中安装软件包：

`pkg_add -l {{path/to/file}}`