# shfmt

> Shell 解析器、格式化器和解释器。
> 更多信息：<https://pkg.go.dev/mvdan.cc/sh>.

- 打印 shell 脚本的格式化版本：

`shfmt {{path/to/file}}`

- 列出未格式化的文件：

`shfmt --list {{path/to/directory}}`

- 将结果写入文件而不是打印到终端：

`shfmt --write {{path/to/file}}`

- 简化代码，去除多余的语法元素（例如，从表达式中的变量前移除 "$"）：

`shfmt --simplify {{path/to/file}}`
