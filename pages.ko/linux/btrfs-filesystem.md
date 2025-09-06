# btrfs filesystem

> btrfs 파일 시스템 관리.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- 파일 시스템 사용량 표시 (상세 정보를 보려면 root로 실행):

`btrfs filesystem usage {{경로/대상/btrfs_마운트}}`

- 개별 장치별 사용량 표시:

`sudo btrfs filesystem show {{경로/대상/btrfs_마운트}}`

- btrfs 파일 시스템에서 단일 파일 조각 모음 (중복 제거 에이전트 실행 중에는 피하십시오):

`sudo btrfs filesystem defragment -v {{경로/대상/파일}}`

- 디렉토리를 재귀적으로 조각 모음 (서브볼륨 경계를 넘지 않음):

`sudo btrfs filesystem defragment -v -r {{경로/대상/폴더}}`

- 미기록된 데이터 블록을 디스크에 강제로 동기화:

`sudo btrfs filesystem sync {{경로/대상/btrfs_마운트}}`

- 디렉토리 내 파일의 디스크 사용량을 재귀적으로 요약:

`sudo btrfs filesystem du --summarize {{경로/대상/폴더}}`
