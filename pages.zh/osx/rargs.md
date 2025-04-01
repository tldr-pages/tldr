# rargs

> 对标准输入的每一行执行一个命令。
> 类似于 `xargs`，但支持模式匹配。
> 更多信息：<https://github.com/lotabout/rargs>。

- 对输入的每一行执行一个命令，就像 `xargs` 一样（`{0}` 表示替换文本的位置）：

`{{command}} | rargs {{command}} {0}`

- 进行预演，打印将要执行的命令而不是真正执行它们：

`{{command}} | rargs -e {{command}} {0}`

- 删除列表中每个文件的 `.bak` 扩展名：

`{{command}} | rargs -p '(.*).bak mv {0} {1}`

- 并行执行命令：

`{{command}} | rargs -w {{max-procs}}`

- 将每一行输入视为由空字符（`\0`）分隔，而不是换行符（`\n`）：

`{{command}} | rargs -0 {{command}} {0}`
