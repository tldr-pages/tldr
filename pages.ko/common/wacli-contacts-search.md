# wacli contacts search

> 이름을 기준으로 WhatsApp 연락처를 검색.
> 관련 항목: `wacli contacts show`, `wacli contacts refresh`.
> 더 많은 정보: <https://wacli.sh/contacts.html>.

- 이름으로 연락처를 검색하고 JSON 형식으로 표시:

`wacli contacts search "{{이름}}" --json`

- 사용자 지정 저장소를 사용하여 이름으로 연락처를 검색:

`wacli contacts search "{{이름}}" --json --store {{경로/대상/저장소}}`
