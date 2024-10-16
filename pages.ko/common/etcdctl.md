# etcdctl

> 고가용성 키-값 쌍 저장소인 `etcd`와 상호작용.
> 더 많은 정보: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

- 지정된 키와 연관된 값을 표시:

`etcdctl get {{자신의_키}}`

- 키-값-쌍을 저장:

`etcdctl put {{자신의_키}} {{자신의_값}}`

- 키-값 쌍 삭제:

`etcdctl del {{자신의_키}}`

- 파일에서 값을 읽어 키-값 쌍을 저장:

`etcdctl put {{자신의_파일}} < {{경로/대상/파일.txt}}`

- etcd 키 저장소의 스냅샷을 저장:

`etcdctl snapshot save {{경로/대상/스냅샷.db}}`

- etcd 키 저장소의 스냅샷을 복원 (나중에 etcd 서버를 다시 시작):

`etcdctl snapshot restore {{경로/대상/스냅샷.db}}`

- 사용자 추가:

`etcdctl user add {{자신의_유저}}`

- 주요 변경사항 살펴보기:

`etcdctl watch {{자신의_키}}`
