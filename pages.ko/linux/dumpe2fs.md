# dumpe2fs

> ext2/ext3/ext4 파일시스템의 슈퍼블록 및 블록 그룹 정보를 출력합니다.
> `umount {{장치}}`를 사용하여 이 명령을 실행하기 전에 파티션을 마운트 해제하세요.
> 더 많은 정보: <https://manned.org/dumpe2fs>.

- ext2, ext3 및 ext4 파일시스템 정보 표시:

`dumpe2fs {{/dev/sdXN}}`

- 파일시스템에서 불량으로 예약된 블록 표시:

`dumpe2fs -b {{/dev/sdXN}}`

- 인식할 수 없는 기능 플래그가 있어도 파일시스템 정보를 강제로 표시:

`dumpe2fs -f {{/dev/sdXN}}`

- 슈퍼블록 정보만 표시하고 블록 그룹 설명자 세부 정보는 표시하지 않음:

`dumpe2fs -h {{/dev/sdXN}}`

- 그룹의 세부 정보 블록 번호를 16진수 형식으로 출력:

`dumpe2fs -x {{/dev/sdXN}}`
