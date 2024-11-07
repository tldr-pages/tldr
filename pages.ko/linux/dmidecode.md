# dmidecode

> DMI(또는 SMBIOS로 알려진) 테이블의 내용을 사람이 읽을 수 있는 형식으로 표시합니다.
> 루트 권한이 필요합니다.
> 더 많은 정보: <https://manned.org/dmidecode>.

- 모든 DMI 테이블 내용을 표시:

`sudo dmidecode`

- BIOS 버전 표시:

`sudo dmidecode -s bios-version`

- 시스템의 일련번호 표시:

`sudo dmidecode -s system-serial-number`

- BIOS 정보 표시:

`sudo dmidecode -t bios`

- CPU 정보 표시:

`sudo dmidecode -t processor`

- 메모리 정보 표시:

`sudo dmidecode -t memory`
