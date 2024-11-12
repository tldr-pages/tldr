# btrfs subvolume

> btrfs 서브볼륨과 스냅샷 관리.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- 새 빈 서브볼륨 생성:

`sudo btrfs subvolume create {{경로/대상/새로운_서브볼륨}}`

- 지정된 파일 시스템의 모든 서브볼륨과 스냅샷 나열:

`sudo btrfs subvolume list {{경로/대상/btrfs_파일시스템}}`

- 서브볼륨 삭제:

`sudo btrfs subvolume delete {{경로/대상/서브볼륨}}`

- 기존 서브볼륨의 읽기 전용 스냅샷 생성:

`sudo btrfs subvolume snapshot -r {{경로/대상/소스_서브볼륨}} {{경로/대상/대상}}`

- 기존 서브볼륨의 읽기-쓰기 스냅샷 생성:

`sudo btrfs subvolume snapshot {{경로/대상/소스_서브볼륨}} {{경로/대상/대상}}`

- 서브볼륨에 대한 자세한 정보 표시:

`sudo btrfs subvolume show {{경로/대상/서브볼륨}}`
