# nasm

> 通用汇编器，一个可移植的 80x86 汇编器。
> 更多信息：<https://nasm.us>。

- 将 `source.asm` 汇编为二进制文件 `source`，使用（默认的）原始二进制格式：

`nasm {{source.asm}}`

- 将 `source.asm` 汇编为指定格式的二进制文件 `output_file`：

`nasm -f {{format}} {{source.asm}} -o {{output_file}}`

- 列出有效的输出格式（同时显示基本的 nasm 帮助信息）：

`nasm -hf`

- 汇编并生成汇编列表文件：

`nasm -l {{list_file}} {{source.asm}}`

- 在汇编前将目录（必须以斜杠结尾）添加到包含文件搜索路径中：

`nasm -i {{path/to/include_dir/}} {{source.asm}}`
