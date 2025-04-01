# iverilog

> 预处理并编译 Verilog HDL (IEEE-1364) 代码，生成用于仿真的可执行程序。
> 更多信息：<https://github.com/steveicarus/iverilog>。

- 将源文件编译成可执行文件：

`iverilog {{path/to/source.v}} -o {{path/to/executable}}`

- 编译源文件时显示所有警告：

`iverilog {{path/to/source.v}} -Wall -o {{path/to/executable}}`

- 使用 VVP 运行时显式编译并运行：

`iverilog -o {{path/to/executable}} -tvvp {{path/to/source.v}}`

- 使用来自不同路径的 Verilog 库文件进行编译：

`iverilog {{path/to/source.v}} -o {{path/to/executable}} -I{{path/to/library_directory}}`

- 预处理 Verilog 代码但不编译：

`iverilog -E {{path/to/source.v}}`
