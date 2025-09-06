# mkfs.ntfs

> 파티션 내에 NTFS 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.ntfs>.

- 장치 b의 파티션 1 (`sdb1`) 에 NTFS 파일 시스템 생성:

`mkfs.ntfs {{/dev/sdb1}}`

- 볼륨 레이블을 지정하여 파일 시스템 생성:

`mkfs.ntfs -L {{볼륨_레이블}} {{/dev/sdb1}}`

- 특정 UUID로 파일 시스템 생성:

`mkfs.ntfs -U {{UUID}} {{/dev/sdb1}}`
