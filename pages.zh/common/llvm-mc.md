# llvm-mc

> LLVM 机器代码工具。提供了一套用于处理 LLVM 机器代码的工具。
> 是 LLVM 的一部分。
> 更多信息：<https://llvm.org/docs/CommandGuide/llvm-mc.html>。

- 将汇编代码文件编译为包含机器代码的目标文件：

`llvm-mc --filetype=obj -o {{path/to/output.o}} {{path/to/input.s}}`

- 反汇编包含机器代码的目标文件为汇编代码文件：

`llvm-mc --disassemble -o {{path/to/output.s}} {{path/to/input.o}}`

- 将 LLVM 位代码文件编译为汇编代码：

`llvm-mc -o {{path/to/output.s}} {{path/to/input.bc}}`

- 从标准输入流中读取汇编代码并显示其编码到标准输出流：

`echo "{{addl %eax, %ebx}}" | llvm-mc -show-encoding -show-inst`

- 从标准输入流中反汇编指定目标的机器代码：

`echo "{{0xCD 0x21}}" | llvm-mc --disassemble -triple={{target_name}}`