# mktemp

> 创建临时文件或目录。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html>.

- 创建一个空的临时文件并打印其绝对路径：

`mktemp`

- 使用自定义目录（默认为 `$TMPDIR`，或者 `/tmp`）：

`mktemp {{[-p |--tmpdir=]}}{{/path/to/tempdir}}`

- 使用自定义路径模板（`X` 会被替换为随机的字母数字字符）：

`mktemp {{/tmp/example.XXXXXXXX}}`

- 使用自定义文件名模板：

`mktemp -t {{example.XXXXXXXX}}`

- 创建一个带有给定后缀的空临时文件并打印其绝对路径：

`mktemp --suffix {{.ext}}`

- 创建一个空的临时目录并打印其绝对路径：

`mktemp {{[-d|--directory]}}`