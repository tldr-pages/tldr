# qemu-system-riscv64

> Emulate `riscv64` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-riscv.html>.

- Boot a kernel emulating riscv64 architecture:

`qemu-system-riscv64 {{[-M|-machine]}} virt -bios none -kernel {{kernel.elf}}`

- List supported machine types:

`qemu-system-x86_64 {{[-M|-machine]}} help`
