# gnmic

> gNMI 명령줄 클라이언트.
> gNMI 네트워크 장치 구성을 관리하고 운영 데이터를 살펴봄.
> 더 많은 정보: <https://gnmic.openconfig.net/user_guide/configuration_flags/>.

- 장치 기능을 요청:

`gnmic --address {{아이피:포트}} capabilities`

- 장치 기능을 가져오려면 사용자 이름과 비밀번호를 제공:

`gnmic --address {{아이피:포트}} --username {{사용자명}} --password {{비밀번호}} capabilities`

- 특정 경로에서 장치 상태의 스냅샷을 가져옴:

`gnmic -a {{아이피:포트}} get --path {{경로}}`

- 특정 경로에서 장치 상태 업데이트:

`gnmic -a {{아이피:포트}} set --update-path {{경로}} --update-value {{값}}`

- 특정 경로의 하위 트리 아래에서 대상 상태 업데이트를 구독:

`gnmic -a {{아이피:포트}} subscribe --path {{경로}}`
