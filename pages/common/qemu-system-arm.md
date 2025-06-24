# qemu-system-arm

> Emulate `arm` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-arm.html>.

- Boot a kernel emulating `arm` architecture:

`qemu-system-arm {{[-M|-machine]}} virt -bios none -kernel {{kernel.elf}}`

- List supported machine types:

`qemu-system-arm {{[-M|-machine]}} help`
