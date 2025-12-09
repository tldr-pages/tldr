# rusnapshot

> Rust로 작성된 BTRFS 스냅샷 유틸리티.
> 더 많은 정보: <https://github.com/Edu4rdSHL/rusnapshot>.

- 구성 파일을 사용하여 스냅샷 생성:

`sudo rusnapshot --config {{경로/대상/config.toml}} --cr`

- 생성된 스냅샷 나열:

`sudo rusnapshot -c {{경로/대상/config.toml}} --list`

- ID 또는 스냅샷 이름으로 스냅샷 삭제:

`sudo rusnapshot -c {{경로/대상/config.toml}} --del --id {{스냅샷_id}}`

- 모든 `hourly` 스냅샷 삭제:

`sudo rusnapshot -c {{경로/대상/config.toml}} --list --keep {{0}} --clean --kind {{hourly}}`

- 읽기-쓰기 스냅샷 생성:

`sudo rusnapshot -c {{경로/대상/config.toml}} --cr --rw`

- 스냅샷 복원:

`sudo rusnapshot -c {{경로/대상/config.toml}} --id {{스냅샷_id}} --restore`
