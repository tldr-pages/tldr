# zfs

> ZFS 파일 시스템 관리.
> 더 많은 정보: <https://manned.org/zfs>.

- 사용 가능한 모든 ZFS 파일 시스템 나열:

`zfs list`

- 새 ZFS 파일 시스템 생성:

`zfs create {{풀_이름/파일시스템_이름}}`

- ZFS 파일 시스템 삭제:

`zfs destroy {{풀_이름/파일시스템_이름}}`

- ZFS 파일 시스템의 스냅샷 생성:

`zfs snapshot {{풀_이름/파일시스템_이름}}@{{스냅샷_이름}}`

- 파일 시스템에 압축 활성화:

`zfs set compression=on {{풀_이름/파일시스템_이름}}`

- 파일 시스템의 마운트 포인트 변경:

`zfs set mountpoint={{/my/mount/path}} {{풀_이름/파일시스템_이름}}`
