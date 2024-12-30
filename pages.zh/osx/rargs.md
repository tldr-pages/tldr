# rargs

> 对于标准输入的每一行执行一个命令。
> 类似于 `xargs`，但支持模式匹配。
> 更多信息：<https://github.com/lotabout/rargs>。

- 对每一行输入执行一个命令，就像 `xargs` 一样（`{0}` 表示文本中要替换的位置）：

`{{command}} | rargs {{command}} {0}`

- 进行干运行，打印将要执行的命令，而不是实际执行它们：

`{{command}} | rargs -e {{command}} {0}`

- 从列表中的每个文件中移除 `.bak` 扩展名：

`{{command}} | rargs -p '(.*).bak mv {0} {1}`

- 并行执行命令：

`{{command}} | rargs -w {{max-procs}}`

- 将每一行输入视为由 NUL 字符 (`\0`) 而不是换行符 (`\n`) 分隔：

`{{command}} | rargs -0 {{command}} {0}`