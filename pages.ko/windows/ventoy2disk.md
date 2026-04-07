# Ventoy2Disk

> Windows 시스템에서 ISO 파일을 사용해 부팅 가능한 USB를 만드는 도구.
> 더 많은 정보: <https://www.ventoy.net/en/doc_windows_cli.html>.

- 기본 설정(MBR, Secure Boot 활성화)으로 D 드라이브에 Ventoy 설치:

`Ventoy2Disk VTOYCLI /I /Drive:D:`

- GPT 파티션 스타일 사용 및 Secure Boot 비활성화 상태로 Ventoy 설치:

`Ventoy2Disk VTOYCLI /I /Drive:D: /GPT /NOSB`

- 디스크 끝에 4GB 공간을 예약하여 :

`Ventoy2Disk VTOYCLI /I /Drive:D: /R:4096`

- 물리 디스크 1번에 NTFS 파일 시스템으로 Ventoy 설치:

`Ventoy2Disk VTOYCLI /I /PhyDrive:1 /FS:NTFS`

- USB 타입 검사 없이 Ventoy 설치 (내장 디스크용):

`Ventoy2Disk VTOYCLI /I /Drive:D: /NOUSBCheck`

- 기존 설정을 유지하며 D 드라이브의 Ventoy 업데이트:

`Ventoy2Disk VTOYCLI /U /Drive:D:`

- 비파괴 설치를 수행 (기존 데이터 유지):

`Ventoy2Disk VTOYCLI /I /Drive:D: /NonDest`

- 모든 옵션 적용해 Ventoy 설치: GPT, Secure Boot 비활성화, 2GB 예약, NTFS, USB 검사 없음:

`Ventoy2Disk VTOYCLI /I /Drive:D: /GPT /NOSB /R:2048 /FS:NTFS /NOUSBCheck`
