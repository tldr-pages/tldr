# exo storage

> Exoscale Simple Object Storage (SOS) 서비스를 관리.
> 더 많은 정보: <https://community.exoscale.com/product/storage/object-storage/>.

- 새로운 SOS 버킷 생성:

`exo storage mb {{버킷_이름}}`

- 파일을 버킷에 업로드:

`exo storage put {{경로/대상/파일}} {{버킷_이름}}/{{prefix/}}`

- 버킷 내 객체 목록 조회:

`exo storage ls {{버킷_이름}}`

- 버킷으로부터 객체 다운로드 시뮬레이션:

`exo storage get {{버킷_이름}}/{{객체_키}} {{로컬_경로}} --dry-run`

- 객체 메타데이터 관리:

`exo storage metadata add {{버킷_이름}}/{{객체_키}} {{key=value}}`
