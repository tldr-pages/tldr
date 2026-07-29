# bison

> GNU 解析器生成器。
> 更多信息：<https://manned.org/bison>。

- 编译 bison 定义文件：

`bison {{路径/到/file.y}}`

- 以调试模式编译，导致生成的解析器将附加信息写入 `stdout`：

`bison {{[-t|--debug]}} {{路径/到/file.y}}`

- 指定输出文件名：

`bison {{[-o|--output]}} {{路径/到/output.c}} {{路径/到/file.y}}`

- 编译时显示详细信息：

`bison {{[-v|--verbose]}}`
