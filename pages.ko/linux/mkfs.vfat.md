# mkfs.vfat

> 파티션 내에 MS-DOS 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.vfat>.

- 장치 b의 파티션 1 (`sdb1`) 에 vfat 파일 시스템 생성:

`mkfs.vfat {{/dev/sdb1}}`

- 볼륨 이름과 함께 파일 시스템 생성:

`mkfs.vfat -n {{볼륨_이름}} {{/dev/sdb1}}`

- 볼륨 ID와 함께 파일 시스템 생성:

`mkfs.vfat -i {{볼륨_ID}} {{/dev/sdb1}}`

- 2 대신 5개의 파일 할당 테이블 사용:

`mkfs.vfat -f 5 {{/dev/sdb1}}`
