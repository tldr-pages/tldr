# gdc

> 使用GCC作为后端的D编译器。
> 更多信息请访问：<https://wiki.dlang.org/Using_GDC>。

- 创建可执行文件：

`gdc {{path/to/source.d}} -o {{path/to/output_executable}}`

- 打印模块依赖信息：

`gdc -fdeps`

- 生成Ddoc文档：

`gdc -fdoc`

- 生成D接口文件：

`gdc -fintfc`

- 在编译时不链接标准GCC库：

`gdc -nostdlib`