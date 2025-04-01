# picotool

> 管理 Raspberry Pi Pico 开发板。
> 更多信息：<https://github.com/raspberrypi/picotool>。

- 显示当前加载在 Pico 上的程序的信息：

`picotool info`

- 将二进制文件加载到 Pico 上：

`picotool load {{path/to/binary}}`

- 将 ELF 或 BIN 文件转换为 UF2 格式：

`picotool uf2 convert {{path/to/elf_or_bin}} {{path/to/output}}`

- 重启 Pico：

`picotool reboot`

- 列出所有已知寄存器：

`picotool otp list`

- 显示版本信息：

`picotool version`

- 显示帮助信息：

`picotool help`
