# mkfs.xfs

> 파티션 내에 XFS 파일 시스템 생성.
> 더 많은 정보: <https://manned.org/mkfs.xfs>.

- 장치의 파티션 1에 XFS 파일 시스템 생성:

`sudo mkfs.xfs {{/dev/sdX1}}`

- 볼륨 레이블을 사용하여 XFS 파일 시스템 생성:

`sudo mkfs.xfs -L {{볼륨_레이블}} {{/dev/sdX1}}`
