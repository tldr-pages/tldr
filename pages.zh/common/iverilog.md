# iverilog

> 预处理并编译 Verilog HDL（IEEE-1364）代码为可执行程序以进行仿真。
> 更多信息：<https://github.com/steveicarus/iverilog>。

- 将源文件编译成可执行文件：

`iverilog {{path/to/source.v}} -o {{path/to/executable}}`

- 在显示所有警告的同时将源文件编译成可执行文件：

`iverilog {{path/to/source.v}} -Wall -o {{path/to/executable}}`

- 明确使用 VVP 运行时编译和运行：

`iverilog -o {{path/to/executable}} -tvvp {{path/to/source.v}}`

- 使用来自不同路径的 Verilog 库文件进行编译：

`iverilog {{path/to/source.v}} -o {{path/to/executable}} -I{{path/to/library_directory}}`

- 不进行编译而预处理 Verilog 代码：

`iverilog -E {{path/to/source.v}}`