# scalafmt

> Scala 的代码格式化工具。
> 配置存储在 `.scalafmt.conf` 文件中。
> 更多信息: <https://scalameta.org/scalafmt>。

- 递归格式化当前目录下所有 `.scala` 文件：

`scalafmt`

- 使用自定义格式化配置格式化特定文件或目录：

`scalafmt --config {{path/to/.scalafmt.conf}} {{path/to/file_or_directory}} {{path/to/file_or_directory}} {{...}}`

- 检查文件是否格式正确，如果所有文件都符合格式风格，返回 `0`：

`scalafmt --config {{path/to/.scalafmt.conf}} --test`

- 排除文件或目录：

`scalafmt --exclude {{path/to/file_or_directory}} {{...}}`

- 仅格式化当前 Git 分支中已编辑的文件：

`scalafmt --config {{path/to/.scalafmt.conf}} --mode diff`