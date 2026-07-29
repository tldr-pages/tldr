# mktemp

> 创建临时文件或目录。
> 更多信息：<https://man.openbsd.org/mktemp.1>。

- 创建空临时文件并打印其绝对路径：

`mktemp`

- 如果未设置 `$TMPDIR`，则使用自定义目录（默认值因平台而异，通常为 `/tmp`）：

`mktemp -p /{{路径/到/临时目录}}`

- 使用自定义路径模板（`X` 被替换为随机字母数字字符）：

`mktemp {{/tmp/example.XXXXXXXX}}`

- 使用自定义文件名模板：

`mktemp -t {{example.XXXXXXXX}}`

- 创建空临时目录并打印其绝对路径：

`mktemp -d`
