# binwalk

> 固件分析工具。
> 更多信息：<https://github.com/ReFirmLabs/binwalk>。

- 扫描二进制文件：

`binwalk {{path/to/binary}}`

- 从二进制文件中提取文件，并指定输出目录：

`binwalk --extract --directory {{output_directory}} {{path/to/binary}}`

- 递归提取二进制文件中的文件，将递归深度限制为2：

`binwalk --extract --matryoshka --depth {{2}} {{path/to/binary}}`

- 从二进制文件中提取具有指定文件签名的文件：

`binwalk --dd '{{png image:png}}' {{path/to/binary}}`

- 分析二进制文件的熵，并将绘图保存为与二进制文件同名并附加`.png`扩展名的文件：

`binwalk --entropy --save {{path/to/binary}}`

- 在一个命令中结合熵分析、签名分析和操作码分析：

`binwalk --entropy --signature --opcodes {{path/to/binary}}`