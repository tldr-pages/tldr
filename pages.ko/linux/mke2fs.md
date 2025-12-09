# mke2fs

> 파티션 내에 Linux 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mke2fs>.

- 장치 b의 파티션 1(`sdb1`)에 ext2 파일 시스템 생성:

`mkfs -t ext2 {{/dev/sdb1}}`

- 장치 b의 파티션 1(`sdb1`)에 ext3 파일 시스템 생성:

`mkfs -t ext3 {{/dev/sdb1}}`

- 장치 b의 파티션 1(`sdb1`)에 ext4 파일 시스템 생성:

`mkfs -t ext4 {{/dev/sdb1}}`
