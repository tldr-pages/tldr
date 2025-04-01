# verilator

> 将 Verilog 和 SystemVerilog 硬件描述语言（HDL）设计转换为 C++ 或 SystemC 模型，编译后执行。
> 更多信息：<https://veripool.org/guide/latest/>.

- 在当前目录中构建特定的 C 项目：

`verilator --binary --build-jobs 0 -Wall {{path/to/source.v}}`

- 在特定文件夹中创建 C++ 可执行文件：

`verilator --cc --exe --build --build-jobs 0 -Wall {{path/to/source.cpp}} {{path/to/output.v}}`

- 对当前目录中的代码进行 lint 检查：

`verilator --lint-only -Wall`

- 创建关于设计的 XML 输出（文件、模块、实例层次结构、逻辑和数据类型），供其他工具使用：

`verilator --xml-output -Wall {{path/to/output.xml}}`