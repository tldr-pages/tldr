# sed

> 以可脚本化的方式编辑文本。
> 另见：`awk`，`ed`。
> 更多信息：<https://www.freebsd.org/cgi/man.cgi?sed>。

- 在所有输入行中将所有 `apple`（基本正则表达式）替换为 `mango`（基本正则表达式）并将结果打印到 `stdout`：

`{{command}} | sed 's/apple/mango/g'`

- 执行特定的脚本 [f]ile 并将结果打印到 `stdout`：

`{{command}} | sed -f {{path/to/script.sed}}`

- 在对输入行应用包含相关 `w` 函数或标志的命令之前，延迟打开每个文件：

`{{command}} | sed -fa {{path/to/script.sed}}`

- 在所有输入行中将所有 `apple`（扩展正则表达式）替换为 `APPLE`（扩展正则表达式）并将结果打印到 `stdout`：

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- 只打印第一行到 `stdout`：

`{{command}} | sed -n '1p'`

- 在特定文件中将所有 `apple`（基本正则表达式）替换为 `mango`（基本正则表达式）并就地覆盖原始文件：

`sed -i 's/apple/mango/g' {{path/to/file}}`