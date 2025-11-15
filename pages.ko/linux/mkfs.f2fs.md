# mkfs.f2fs

> 파티션 내에 F2FS 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.f2fs>.

- 장치 b의 파티션 1 (`sdb1`) 에 F2FS 파일 시스템 생성:

`sudo mkfs.f2fs {{/dev/sdb1}}`

- 볼륨 레이블을 지정하여 F2FS 파일 시스템 생성:

`sudo mkfs.f2fs -l {{볼륨_레이블}} {{/dev/sdb1}}`
