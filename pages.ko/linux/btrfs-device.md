# btrfs device

> btrfs 파일 시스템에서 장치 관리.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- btrfs 파일 시스템에 하나 이상의 장치 추가:

`sudo btrfs device add {{경로/대상/블록_장치1}} [{{경로/대상/블록_장치2}}] {{경로/대상/btrfs_파일_시스템}}`

- btrfs 파일 시스템에서 장치 제거:

`sudo btrfs device remove {{경로/대상/장치|장치_ID}} [{{...}}]`

- 오류 통계 표시:

`sudo btrfs device stats {{경로/대상/btrfs_파일_시스템}}`

- 모든 디스크를 스캔하고 감지된 모든 btrfs 파일 시스템을 커널에 알림:

`sudo btrfs device scan --all-devices`

- 디스크별 할당 통계 자세히 표시:

`sudo btrfs device usage {{경로/대상/btrfs_파일_시스템}}`
