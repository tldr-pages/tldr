# mkfs.exfat

> 파티션 내에 exfat 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.exfat>.

- 장치 b의 파티션 1 (`sdb1`) 에 exfat 파일 시스템 생성:

`mkfs.exfat {{/dev/sdb1}}`

- 볼륨 이름을 지정하여 파일 시스템 생성:

`mkfs.exfat -n {{볼륨_이름}} {{/dev/sdb1}}`

- 볼륨 ID를 지정하여 파일 시스템 생성:

`mkfs.exfat -i {{볼륨_ID}} {{/dev/sdb1}}`
