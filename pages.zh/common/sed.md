# sed

> 以可脚本化的方式编辑文本。
> 另请参阅：`awk`、`ed`。
> 更多信息：<https://manned.org/sed.1posix>。

- 将所有输入行中的 `apple`（基本正则表达式）替换为 `mango` 并输出到 `stdout`：

`{{命令}} | sed 's/apple/mango/g'`

- 执行指定的脚本文件并输出到 `stdout`：

`{{命令}} | sed -f {{路径/到/脚本.sed}}`

- 仅将第一行输出到 `stdout`：

`{{命令}} | sed -n '1p'`
