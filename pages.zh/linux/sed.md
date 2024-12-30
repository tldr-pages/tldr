# sed

> 以可脚本化的方式编辑文本。
> 另请参见：`awk`，`ed`。
> 更多信息：<https://www.gnu.org/software/sed/manual/sed.html>。

- 在所有输入行中将所有 `apple`（基本正则表达式）出现的地方替换为 `mango`（基本正则表达式），并将结果打印到 `stdout`：

`{{command}} | sed 's/apple/mango/g'`

- 在所有输入行中将所有 `apple`（扩展正则表达式）出现的地方替换为 `APPLE`（扩展正则表达式），并将结果打印到 `stdout`：

`{{command}} | sed -E 's/(apple)/\U\1/g'`

- 在特定文件中将所有 `apple`（基本正则表达式）出现的地方替换为 `mango`（基本正则表达式），并就地覆盖原始文件：

`sed -i 's/apple/mango/g' {{path/to/file}}`

- 执行特定脚本 [f]ile 并将结果打印到 `stdout`：

`{{command}} | sed -f {{path/to/script.sed}}`

- 只打印第一行到 `stdout`：

`{{command}} | sed -n '1p'`

- [d]elete 文件的第一行：

`sed -i 1d {{path/to/file}}`

- [i]nsert 在文件的第一行插入新行：

`sed -i '1i\your new line text\' {{path/to/file}}`