# kernelstub

> (U)EFI 환경에서 Linux 커널 부팅 구성을 자동으로 관리.
> 더 많은 정보: <https://github.com/isantop/kernelstub#usage>.

- 기본 옵션으로 현재 커널 구성:

`sudo kernelstub`

- 사용자 지정 커널 옵션 추가:

`sudo kernelstub {{[-o|--options]}} "{{quiet splash mitigations=off}}"`

- 상세 출력과 함께 `systemd-boot` 설정 사용:

`sudo kernelstub {{[-v|--verbose]}} {{[-l|--loader]}}`

- NVRAM은 변경 없이 ESP에 커널만 복사:

`sudo kernelstub {{[-m|--manage-only]}}`

- 실제 변경 없이 시뮬레이션 실행:

`sudo kernelstub {{[-c|--dry-run]}}`

- 커널, initrd 및 ESP 경로를 직접 지정:

`sudo kernelstub {{[-k|--kernel-path]}} /{{경로/대상/vmlinuz}} {{[-i|--initrd-path]}} /{{경로/대상/initrd.img}} {{[-e|--esp-path]}} /{{경로/대상/efi_partition}}`

- 현재 설정 표시:

`sudo kernelstub {{[-p|--print-config]}}`
