# qemu-system-riscv64

> Emula a arquitetura `riscv64`.
> Mais informações: <https://www.qemu.org/docs/master/system/target-riscv.html>.

- Inicializa um kernel emulando a arquitetura `riscv64`:

`qemu-system-riscv64 {{[-M|-machine]}} virt -bios none -kernel {{kernel.elf}} -nographic`

- Lista os tipos de máquina suportados:

`qemu-system-riscv64 {{[-M|-machine]}} help`

- Sai do QEMU sem gráficos:

`<Ctrl a><x>`
