# qemu-system-riscv64

> Emulate `riscv64` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-riscv.html>.

- Boot a kernel emulating `riscv64` architecture:

`qemu-system-riscv64 {{[-M|-machine]}} virt -bios none -kernel {{kernel.elf}} -nographic`

- List supported machine types:

`qemu-system-riscv64 {{[-M|-machine]}} help`

- Exit non-graphical QEMU:

`<Ctrl a><x>`
