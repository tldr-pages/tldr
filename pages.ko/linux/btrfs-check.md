# btrfs check

> btrfs 파일 시스템 검사 또는 복구.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- btrfs 파일 시스템 검사:

`sudo btrfs check {{경로/대상/파티션}}`

- btrfs 파일 시스템 검사 및 복구 (위험함):

`sudo btrfs check --repair {{경로/대상/파티션}}`

- 검사 진행 상황 표시:

`sudo btrfs check --progress {{경로/대상/파티션}}`

- 각 데이터 블록의 체크섬 확인 (파일 시스템이 손상되지 않은 경우):

`sudo btrfs check --check-data-csum {{경로/대상/파티션}}`

- `n`번째 슈퍼블록 사용 (`n`은 0, 1 또는 2 가능):

`sudo btrfs check --super {{n}} {{경로/대상/파티션}}`

- 체크섬 트리 재구성:

`sudo btrfs check --repair --init-csum-tree {{경로/대상/파티션}}`

- 익스텐트 트리 재구성:

`sudo btrfs check --repair --init-extent-tree {{경로/대상/파티션}}`
