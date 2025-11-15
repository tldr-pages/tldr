# btrfs inspect-internal

> btrfs 파일 시스템의 내부 정보를 쿼리.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- 슈퍼블록 정보 출력:

`sudo btrfs inspect-internal dump-super {{경로/대상/파티션}}`

- 슈퍼블록 및 모든 복사본의 정보 출력:

`sudo btrfs inspect-internal dump-super --all {{경로/대상/파티션}}`

- 파일 시스템 메타데이터 정보 출력:

`sudo btrfs inspect-internal dump-tree {{경로/대상/파티션}}`

- `n`번째 inode의 파일 목록 출력:

`sudo btrfs inspect-internal inode-resolve {{n}} {{경로/대상/btrfs_마운트}}`

- 지정된 논리 주소에 있는 파일 목록 출력:

`sudo btrfs inspect-internal logical-resolve {{논리_주소}} {{경로/대상/btrfs_마운트}}`

- 루트, extent, csum 및 fs 트리의 통계 출력:

`sudo btrfs inspect-internal tree-stats {{경로/대상/파티션}}`
