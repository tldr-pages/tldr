# CONFIG

> 런타임 중 DOSBox 설정을 변경하거나 조회 및 설정/언어 파일을 저장하는 명령어.
> 더 많은 정보: <https://www.dosbox.com/wiki/CONFIG>.

- 현재 설정을 파일로 저장 (로컬 드라이브):

`CONFIG -writeconf {{경로/대상/파일.conf}}`

- 현재 언어 문자열을 파일로 저장:

`CONFIG -writelang {{경로/대상/파일.lang}}`

- 보안 모드 활성화 (MOUNT/IMGMOUNT/BOOT 비활성화):

`CONFIG -securemode`

- 설정 값 변경 (예: CPU cycles):

`CONFIG -set "cpu cycles={{10000}}"`

- 설정 값 변경 (예: EMS 비활성화):

`CONFIG -set "dos ems=off"`

- 설정 값 조회 (`%CONFIG%`에 저장됨):

`CONFIG -get "cpu core"`
