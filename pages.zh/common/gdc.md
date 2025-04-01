# gdc

> 以 GCC 作为后端的 D 语言编译器。
> 更多信息：<https://wiki.dlang.org/Using_GDC>。

- 创建可执行文件：

`gdc {{path/to/source.d}} -o {{path/to/output_executable}}`

- 打印模块依赖信息：

`gdc -fdeps`

- 生成 Ddoc 文档：

`gdc -fdoc`

- 生成 D 接口文件：

`gdc -fintfc`

- 编译时不链接标准 GCC 库：

`gdc -nostdlib`
