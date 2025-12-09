# btrfs property

> BTRFS 파일 시스템 객체(파일, 디렉터리, 서브볼륨, 파일 시스템 또는 장치)에 대한 속성을 가져오거나 설정하거나 나열합니다.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- 주어진 btrfs 객체에 대해 사용 가능한 속성(및 설명)을 나열:

`sudo btrfs property list {{경로/대상/btrfs_객체}}`

- 주어진 btrfs 객체의 모든 속성을 가져오기:

`sudo btrfs property get {{경로/대상/btrfs_객체}}`

- 주어진 btrfs 파일 시스템 또는 장치의 `label` 속성을 가져오기:

`sudo btrfs property get {{경로/대상/btrfs_파일시스템}} label`

- 주어진 btrfs 파일 시스템 또는 장치의 모든 객체 유형별 속성을 가져오기:

`sudo btrfs property get -t {{subvol|filesystem|inode|device}} {{경로/대상/btrfs_파일시스템}}`

- 주어진 btrfs inode(파일 또는 디렉터리)의 `compression` 속성을 설정:

`sudo btrfs property set {{경로/대상/btrfs_inode}} compression {{zstd|zlib|lzo|none}}`
