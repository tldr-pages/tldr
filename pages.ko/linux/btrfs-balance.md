# btrfs balance

> btrfs 파일 시스템에서 블록 그룹을 균형 조정.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- 실행 중이거나 일시 중지된 균형 조정 작업 상태 표시:

`sudo btrfs balance status {{경로/대상/btrfs_파일시스템}}`

- 모든 블록 그룹 균형 조정 (느림; 파일 시스템의 모든 블록을 다시 씀):

`sudo btrfs balance start {{경로/대상/btrfs_파일시스템}}`

- 사용률이 15% 미만인 데이터 블록 그룹을 백그라운드에서 균형 조정:

`sudo btrfs balance start --bg -dusage={{15}} {{경로/대상/btrfs_파일시스템}}`

- 주어진 장치 `devid`에 사용률 20% 미만이고 최소 1개의 청크가 있는 최대 10개의 메타데이터 청크 균형 조정 (btrfs filesystem show 참고):

`sudo btrfs balance start -musage={{20}},limit={{10}},devid={{devid}} {{경로/대상/btrfs_파일시스템}}`

- 데이터 블록을 raid6로, 메타데이터를 raid1c3로 변환 (프로필은 mkfs.btrfs(8) 참고):

`sudo btrfs balance start -dconvert={{raid6}} -mconvert={{raid1c3}} {{경로/대상/btrfs_파일시스템}}`

- 이미 변환된 청크를 건너뛰고 데이터 블록을 raid1로 변환 (예: 이전에 취소된 변환 작업 후):

`sudo btrfs balance start -dconvert={{raid1}},soft {{경로/대상/btrfs_파일시스템}}`

- 실행 중이거나 일시 중지된 균형 조정 작업 취소, 일시 중지 또는 재개:

`sudo btrfs balance {{cancel|pause|resume}} {{경로/대상/btrfs_파일시스템}}`
