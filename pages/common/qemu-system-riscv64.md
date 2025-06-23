# qemu-system-riscv64

> Emulate `riscv64` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-riscv.html>.

- Boot a kernel emulating riscv64 architecture:

`qemu-system-riscv64 -machine virt -bios none -kernel {{kernel.elf}}`
