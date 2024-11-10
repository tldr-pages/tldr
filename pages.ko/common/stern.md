# stern

> Kubernetes의 여러 팟 및 컨테이너 로그를 동시에 확인.
> 더 많은 정보: <https://github.com/stern/stern>.

- 현재 네임스페이스 내의 모든 팟 로그 확인:

`stern .`

- 특정 상태의 모든 팟 로그 확인:

`stern . --container-state {{running|waiting|terminated}}`

- 주어진 정규 표현식과 일치하는 모든 팟 로그 확인:

`stern {{팟_쿼리}}`

- 모든 네임스페이스에서 일치하는 팟 로그 확인:

`stern {{팟_쿼리}} --all-namespaces`

- 15분 전부터 일치하는 팟 로그 확인:

`stern {{팟_쿼리}} --since {{15m}}`

- 특정 레이블이 있는 일치하는 팟 로그 확인:

`stern {{팟_쿼리}} --selector {{release=canary}}`
