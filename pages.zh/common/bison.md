# bison

> GNU 解析器生成器。
> 更多信息：<https://manned.org/bison>.

- 编译一个 bison 定义文件：

`bison {{path/to/file.y}}`

- 以调试模式编译，这会导致生成的解析器将额外信息写入 `stdout`：

`bison {{[-t|--debug]}} {{path/to/file.y}}`

- 指定输出文件名：

`bison {{[-o|--output]}} {{path/to/output.c}} {{path/to/file.y}}`

- 编译时详细输出：

`bison {{[-v|--verbose]}}`