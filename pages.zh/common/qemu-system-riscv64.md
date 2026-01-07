# qemu-system-riscv64

> 模拟 `riscv64` 架构。
> 更多信息：<https://www.qemu.org/docs/master/system/target-riscv.html>。

- 启动一个模拟 `riscv64` 架构的内核：

`qemu-system-riscv64 {{[-M|-machine]}} virt -bios none -kernel {{kernel.elf}} -nographic`

- 列出支持的机器类型：

`qemu-system-riscv64 {{[-M|-machine]}} help`

- 退出无图形界面的 QEMU：

`<Ctrl a><x>`
