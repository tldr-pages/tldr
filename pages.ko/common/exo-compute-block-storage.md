# exo compute block-storage

> Exoscale Block Storage 서비스 관리.
> 더 많은 정보: <https://community.exoscale.com/product/storage/block-storage/>.

- 20GB Block Storage 볼륨 생성:

`exo compute block-storage create {{volume_name}} --size 20 {{[-z|--zone]}} {{zone}}`

- Block Storage 볼륨 목록 조회:

`exo compute block-storage list`

- Block Storage 볼륨을 Compute 인스턴스에 연결:

`exo compute block-storage attach {{볼륨_이름_또는_아이디}} {{인스턴스_이름_또는_아이디}} {{[-z|--zone]}} {{zone}}`

- Block Storage 볼륨 강제 분리 (확인 없이 실행):

`exo compute block-storage detach {{볼륨_이름_또는_아이디}} {{[-z|--zone]}} {{zone}} {{[-f|--force]}}`

- Block Storage 볼륨 스냅샷 생성:

`exo compute block-storage snapshot create {{볼륨_이름_또는_아이디}} --name {{스냅샷_이름}} {{[-z|--zone]}} {{zone}}`

- 스냅샷을 기반으로 Block Storage 볼륨 생성:

`exo compute block-storage create {{볼륨_이름}} --snapshot {{스냅샷_이름_또는_아이디}} {{[-z|--zone]}} {{zone}}`

- 기존 Block Storage 볼륨 이름 변경 및 30GB으로 크기 업데이트:

`exo compute block-storage update {{볼륨_이름_또는_아이디}} --size 30 --name {{새로운_이름}}`
