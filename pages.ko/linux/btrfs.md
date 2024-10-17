# btrfs

> Linux용으로 설계된 카피 온 라이트(COW) 원칙 기반 파일 시스템.
> `device`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- 서브볼륨 생성:

`sudo btrfs subvolume create {{경로/대상/서브볼륨}}`

- 서브볼륨 목록 나열:

`sudo btrfs subvolume list {{경로/대상/마운트_포인트}}`

- 공간 사용 정보 표시:

`sudo btrfs filesystem df {{경로/대상/마운트_포인트}}`

- 쿼터 활성화:

`sudo btrfs quota enable {{경로/대상/서브볼륨}}`

- 쿼터 표시:

`sudo btrfs qgroup show {{경로/대상/서브볼륨}}`
