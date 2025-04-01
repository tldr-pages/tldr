# mktemp

> 创建临时文件或目录。
> 更多信息：<https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- 创建一个空的临时文件并打印其绝对路径：

`mktemp`

- 使用自定义目录（默认为 `getconf DARWIN_USER_TEMP_DIR` 的输出，或 `/tmp`）：

`mktemp --tmpdir={{/path/to/tempdir}}`

- 使用自定义路径模板（`X` 会被随机的字母数字字符替换）：

`mktemp {{/tmp/example.XXXXXXXX}}`

- 使用自定义文件名前缀：

`mktemp -t {{example}}`

- 创建一个空的临时目录并打印其绝对路径：

`mktemp --directory`