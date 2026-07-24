# qemu-system-riscv64

> `riscv64` 아키텍처를 에뮬레이션.
> 더 많은 정보: <https://www.qemu.org/docs/master/system/target-riscv.html>.

- `riscv64` 아키텍처를 에뮬레이션하여 커널 부팅:

`qemu-system-riscv64 {{[-M|-machine]}} virt -bios none -kernel {{커널.elf}} -nographic`

- 지원되는 머신 타입 목록 표시:

`qemu-system-riscv64 {{[-M|-machine]}} help`

- 비그래픽 모드의 QEMU 종료:

`<Ctrl a><x>`
