# mktemp

> 创建一个临时文件或目录。
> 更多信息：<https://man.openbsd.org/mktemp.1>。

- 创建一个空的临时文件并打印其绝对路径：

`mktemp`

- 如果未设置 `$TMPDIR`，则使用自定义目录（默认值依赖于平台，但通常为 `/tmp`）：

`mktemp -p {{/path/to/tempdir}}`

- 使用自定义路径模板（`X` 被随机的字母数字字符替换）：

`mktemp {{/tmp/example.XXXXXXXX}}`

- 使用自定义文件名模板：

`mktemp -t {{example.XXXXXXXX}}`

- 创建一个空的临时目录并打印其绝对路径：

`mktemp -d`