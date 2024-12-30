# shfmt

> Shell 解析器、格式化工具和解释器。
> 更多信息：<https://pkg.go.dev/mvdan.cc/sh>。

- 打印格式化后的 shell 脚本版本：

`shfmt {{path/to/file}}`

- 列出未格式化的文件：

`shfmt --list {{path/to/directory}}`

- 将结果写入文件，而不是打印到终端：

`shfmt --write {{path/to/file}}`

- 简化代码，删除冗余的语法部分（即从表达式中的变量中删除 "$"）：

`shfmt --simplify {{path/to/file}}`