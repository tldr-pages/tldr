# mkfs.cramfs

> 파티션 내에 ROM 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.cramfs>.

- 장치 b의 파티션 1 (`sdb1`) 에 ROM 파일 시스템 생성:

`mkfs.cramfs {{/dev/sdb1}}`

- 볼륨 이름을 지정하여 ROM 파일 시스템 생성:

`mkfs.cramfs -n {{볼륨_이름}} {{/dev/sdb1}}`
