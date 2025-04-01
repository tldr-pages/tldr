# pwn

> 用于快速原型设计的漏洞开发库。
> 更多信息：<https://docs.pwntools.com/en/stable/commandline.html>。

- 将给定的汇编代码转换为 `字节`：

`pwn asm "{{xor edi, edi}}"`

- 创建特定长度的循环模式：

`pwn cyclic {{number}}`

- 将给定的数据编码为十六进制：

`pwn hex {{deafbeef}}`

- 将给定的数据从十六进制解码：

`pwn unhex {{6c4f7645}}`

- 打印用于运行 shell 的 x64 Linux shellcode：

`pwn shellcraft {{amd64.linux.sh}}`

- 检查给定的 ELF 文件的二进制安全设置：

`pwn checksec {{path/to/file}}`

- 检查 Pwntools 更新：

`pwn update`

- 显示版本：

`pwn version`
