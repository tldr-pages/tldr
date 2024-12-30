# sed

> 以可脚本化的方式编辑文本。
> 另见：`awk`，`ed`。
> 更多信息：<https://keith.github.io/xcode-man-pages/sed.1.html>。

- 在所有输入行中将所有 `apple`（基本正则表达式）替换为 `mango`（基本正则表达式），并将结果打印到 `stdout`：

`{{command}} | sed 's/apple/mango/g'`

- 执行特定的脚本 [f]ile，并将结果打印到 `stdout`：

`{{command}} | sed -f {{path/to/script_file.sed}}`

- 在所有输入行中将所有 `apple`（扩展正则表达式）替换为 `APPLE`（扩展正则表达式），并将结果打印到 `stdout`：

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- 只打印第一行到 `stdout`：

`{{command}} | sed -n '1p'`

- 在 `file` 中将所有 `apple`（基本正则表达式）替换为 `mango`（基本正则表达式），并将原始文件备份到 `file.bak`：

`sed -i bak 's/apple/mango/g' {{path/to/file}}`