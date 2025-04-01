# sed

> 以脚本方式编辑文本。
> 参见：`awk`，`ed`。
> 更多信息：<https://manned.org/sed.1posix>。

- 将所有输入行中的 `apple`（基本正则表达式）替换为 `mango`（基本正则表达式），并将结果打印到 `stdout`：

`{{command}} | sed 's/apple/mango/g'`

- 执行特定的脚本 [f]ile，并将结果打印到 `stdout`：

`{{command}} | sed -f {{path/to/script.sed}}`

- 只将第一行打印到 `stdout`：

`{{command}} | sed -n '1p'`