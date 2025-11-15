# zdb

> ZFS 디버거.
> 더 많은 정보: <https://manned.org/zdb>.

- 모든 마운트된 ZFS zpool의 상세 설정 보기:

`zdb`

- 특정 ZFS 풀의 상세 설정 보기:

`zdb -C {{풀명}}`

- 블록의 수, 크기 및 중복 제거에 대한 통계 보기:

`zdb -b {{풀명}}`
