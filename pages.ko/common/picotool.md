# picotool

> Raspberry Pi Pico 보드 관리.
> 더 많은 정보: <https://github.com/raspberrypi/picotool#overview>.

- 현재 Pico에 로그된 프로그램 정보 표시:

`picotool info`

- Pico에 바이너리 로드:

`picotool load {{경로/대상/바이너리}}`

- ELF 또는 BIN 파일을 UF2 형식으로 변환:

`picotool uf2 convert {{경로/대상/elf_또는_bin}} {{경로/대상/출력파일}}`

- Pico 재부팅:

`picotool reboot`

- 알려진 모든 레지스터 목록 표시:

`picotool otp list`

- 도움말 표시:

`picotool help`

- 버전 정보 표시:

`picotool version`
