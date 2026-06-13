# mkfs.ext4

> 파티션 내에 ext4 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.ext4>.

- 장치 b의 파티션 1 (`sdb1`) 에 ext4 파일 시스템 생성:

`sudo mkfs.ext4 {{/dev/sdb1}}`

- 볼륨 라벨을 지정하여 ext4 파일 시스템 생성:

`sudo mkfs.ext4 -L {{볼륨_라벨}} {{/dev/sdb1}}`
