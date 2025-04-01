# ghdl

> VHDL 语言的开源仿真器。
> 更多信息：<https://ghdl.github.io/ghdl/>.

- 分析 VHDL 源文件并生成目标文件：

`ghdl -a {{filename.vhdl}}`

- 展开设计（其中 `design` 是配置单元、实体单元或结构体单元的名称）：

`ghdl -e {{design}}`

- 运行已展开的设计：

`ghdl -r {{design}}`

- 运行已展开的设计并将输出转储到波形文件中：

`ghdl -r {{design}} --wave={{output.ghw}}`

- 检查 VHDL 源文件的语法：

`ghdl -s {{filename.vhdl}}`

- 显示帮助：

`ghdl --help`
