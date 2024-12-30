# pwn

> 针对快速原型开发的漏洞开发库。
> 更多信息：<https://docs.pwntools.com/en/stable/commandline.html>。

- 将给定的汇编代码转换为 `bytes`：

`pwn asm "{{xor edi, edi}}"`

- 创建特定字符数量的循环模式：

`pwn cyclic {{number}}`

- 将给定数据编码为十六进制系统：

`pwn hex {{deafbeef}}`

- 从十六进制解码给定数据：

`pwn unhex {{6c4f7645}}`

- 打印一个用于运行 shell 的 x64 Linux shellcode：

`pwn shellcraft {{amd64.linux.sh}}`

- 检查给定 ELF 文件的二进制安全设置：

`pwn checksec {{path/to/file}}`

- 检查 Pwntools 更新：

`pwn update`

- 显示版本：

`pwn version`