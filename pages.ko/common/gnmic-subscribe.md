# gnmic subscribe

> gnmic 네트워크 장치 상태 업데이트를 구독.
> 더 많은 정보: <https://gnmic.kmrd.dev/cmd/subscribe>.

- 특정 경로의 하위 트리 아래에서 대상 상태 업데이트를 구독:

`gnmic --address {{아이피:포트}} subscribe --path {{경로}}`

- 샘플 간격이 30초인 대상을 구독 (기본값 10초):

`gnmic -a {{아이피:포트}} subscribe --path {{경로}} --sample-interval 30s`

- 샘플 간격으로 대상을 구독하고 변경 시에만 업데이트:

`gnmic -a {{아이피:포트}} subscribe --path {{경로}} --stream-mode on-change --heartbeat-interval 1m`

- 단 한 번의 업데이트만을 위해 대상을 구독:

`gnmic -a {{아이피:포트}} subscribe --path {{경로}} --mode once`

- 대상을 구독하고 응답 인코딩을 지정 (json_ietf):

`gnmic -a {{아이피:포트}} subscribe --path {{경로}} --encoding json_ietf`
