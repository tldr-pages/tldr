# btrfs restore

> 손상된 btrfs 파일 시스템에서 파일을 복구하려고 시도합니다.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- btrfs 파일 시스템에서 모든 파일을 지정된 디렉토리로 복원:

`sudo btrfs restore {{경로/대상/btrfs_장치}} {{경로/대상/대상_폴더}}`

- btrfs 파일 시스템에서 복원할 파일 목록 표시 (복원하지 않음):

`sudo btrfs restore --dry-run {{경로/대상/btrfs_장치}} {{경로/대상/대상_폴더}}`

- 주어진 정규 표현식과 일치하는 파일을 btrfs 파일 시스템에서 복원 ([대]소문자 구분 없음, 대상 파일의 모든 상위 디렉토리도 일치해야 함):

`sudo btrfs restore --path-regex {{정규식}} -c {{경로/대상/btrfs_장치}} {{경로/대상/대상_폴더}}`

- 특정 루트 트리 `bytenr`를 사용하여 btrfs 파일 시스템에서 파일 복원 (`btrfs-find-root` 참조):

`sudo btrfs restore -t {{bytenr}} {{경로/대상/btrfs_장치}} {{경로/대상/대상_폴더}}`

- btrfs 파일 시스템에서 메타데이터, 확장 속성, 심볼릭 링크와 함께 파일을 복원하여 대상의 파일을 덮어쓰기:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{경로/대상/btrfs_장치}} {{경로/대상/대상_폴더}}`
