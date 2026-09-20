# testdisk

> 디스크 파티션을 검사하고 복구.
> 관련 항목: `photorec`, `fdisk`.
> 더 많은 정보: <https://manned.org/testdisk>.

- 지정한 장치에서 TestDisk 실행:

`sudo testdisk {{/dev/sdX}}`

- 디스크 이미지에서 TestDisk 실행:

`sudo testdisk {{경로/대상/이미지.dd}}`

- 로그 파일을 생성하며 TestDisk 실행 (`testdisk.log`):

`sudo testdisk /log {{/dev/sdX}}`

- 현재 파티션 목록 표시:

`sudo testdisk /list`

- 버전 정보 표시:

`testdisk /version`
