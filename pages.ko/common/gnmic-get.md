# gnmic get

> gnmi 네트워크 장치 작동 데이터의 스냅샷 가져오기.
> 더 많은 정보: <https://gnmic.kmrd.dev/cmd/get>.

- 특정 경로에서 장치 상태의 스냅샷을 가져옴:

`gnmic --address {{아이피:포트}} get --path {{경로}}`

- 여러 경로에서 장치 상태를 쿼리:

`gnmic -a {{아이피:포트}} get --path {{경로/대상/파일_또는_디렉터리1}} --path {{경로/대상/파일_또는_디렉터리2}}`

- 공통 접두사를 사용하여 여러 경로에서 장치 상태를 쿼리:

`gnmic -a {{아이피:포트}} get --prefix {{접두사}} --path {{경로/대상/파일_또는_디렉터리1}} --path {{경로/대상/파일_또는_디렉터리2}}`

- 장치 상태를 쿼리하고 응답 인코딩을 지정 (json_ietf):

`gnmic -a {{아이피:포트}} get --path {{경로}} --encoding json_ietf`
