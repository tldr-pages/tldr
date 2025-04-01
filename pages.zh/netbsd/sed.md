# sed

> 以脚本方式编辑文本。
> 参见: `awk`, `ed`。
> 更多信息: <https://man.netbsd.org/sed.1>。

- 将所有输入行中的 `apple`（基本正则表达式）替换为 `mango`（基本正则表达式），并将结果输出到 `stdout`：

`{{command}} | sed 's/apple/mango/g'`

- 执行特定的脚本 [f]ile，并将结果输出到 `stdout`：

`{{command}} | sed -f {{path/to/script.sed}}`

- 延迟打开每个文件，直到包含相关 `w` 函数或标志的命令应用于输入行：

`{{command}} | sed -fa {{path/to/script.sed}}`

- 启用 GNU 正则表达式扩展：

`{{command}} | sed -fg {{path/to/script.sed}}`

- 将所有输入行中的 `apple`（扩展正则表达式）替换为 `APPLE`（扩展正则表达式），并将结果输出到 `stdout`：

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- 只将第一行输出到 `stdout`：

`{{command}} | sed -n '1p'`

- 将特定文件中的所有 `apple`（基本正则表达式）替换为 `mango`（基本正则表达式），并就地覆盖原始文件：

`sed -i 's/apple/mango/g' {{path/to/file}}`