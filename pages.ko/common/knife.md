# knife

> 로컬 Chef 저장소에서 Chef 서버와 상호 작용.
> 더 많은 정보: <https://docs.chef.io/knife.html>.

- 새 노드 부트스트랩:

`knife bootstrap {{fqdn_또는_ip}}`

- 등록된 모든 노드 나열:

`knife node list`

- 노드 표시:

`knife node show {{노드_이름}}`

- 노드 편집:

`knife node edit {{노드_이름}}`

- 역할 편집:

`knife role edit {{역할_이름}}`

- 데이터 백 보기:

`knife data bag show {{데이터_백_이름}} {{데이터_백_항목}}`

- 로컬 쿠크북을 Chef 서버에 업로드:

`knife cookbook upload {{쿠크북_이름}}`
