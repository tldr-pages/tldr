# etcd

> 분산 시스템의 가장 중요한 데이터를 위한, 신뢰할 수 있는 분산 키-값 저장소.
> 더 많은 정보: <https://etcd.io>.

- 단일 노드 etcd 클러스터를 시작:

`etcd`

- 단일 노드 etcd 클러스터를 시작하고, 사용자 정의 URL에서 클라이언트 요청을 수신:

`etcd --advertise-client-urls {{http://127.0.0.1:1234}} --listen-client-urls {{http://127.0.0.1:1234}}`

- 사용자 정의 이름으로 단일 노드 etcd 클러스터를 시작:

`etcd --name {{내_etcd_클러스터}}`

- <http://localhost:2379/debug/pprof/>에서 사용할 수 있는 광범위한 측정항목을 사용하여, 단일 노드 etcd 클러스터를 시작:

`etcd --enable-pprof --metrics extensive`
