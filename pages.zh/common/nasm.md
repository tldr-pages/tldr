# nasm

> Netwide汇编器，一个便携式80x86汇编器。
> 更多信息：<https://nasm.us>。

- 将`source.asm`汇编成一个二进制文件`source`，采用（默认）原始二进制格式：

`nasm {{source.asm}}`

- 将`source.asm`汇编成一个二进制文件`output_file`，采用指定格式：

`nasm -f {{format}} {{source.asm}} -o {{output_file}}`

- 列出有效的输出格式（以及基本的nasm帮助信息）：

`nasm -hf`

- 汇编并生成汇编列表文件：

`nasm -l {{list_file}} {{source.asm}}`

- 在汇编之前，将一个目录（必须以斜杠结尾）添加到包含文件搜索路径中：

`nasm -i {{path/to/include_dir/}} {{source.asm}}`