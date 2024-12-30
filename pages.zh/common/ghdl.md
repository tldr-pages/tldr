# ghdl

> VHDL语言的开源模拟器。
> 更多信息：<https://ghdl.github.io/ghdl/>

- 分析VHDL源文件并生成对象文件：

`ghdl -a {{filename.vhdl}}`

- 详细说明设计（其中 `design` 是配置单元、实体单元或架构单元的名称）：

`ghdl -e {{design}}`

- 运行详细说明的设计：

`ghdl -r {{design}}`

- 运行详细说明的设计并将输出转储到波形文件：

`ghdl -r {{design}} --wave={{output.ghw}}`

- 检查VHDL源文件的语法：

`ghdl -s {{filename.vhdl}}`

- 显示帮助：

`ghdl --help`