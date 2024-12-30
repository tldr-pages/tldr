# systemd-path

> 列出和查询系统和用户路径。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-path.html>。

- 显示已知路径及其当前值的列表：

`systemd-path`

- 查询指定路径并显示其值：

`systemd-path "{{path_name}}"`

- 在打印的路径后附加 `suffix_string`：

`systemd-path --suffix {{suffix_string}}`

- 打印简短版本字符串然后退出：

`systemd-path --version`