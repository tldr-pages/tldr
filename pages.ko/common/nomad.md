# nomad

> 분산형, 고가용성, 데이터센터 인식 스케줄러.
> 더 많은 정보: <https://www.nomadproject.io/docs/commands/>.

- 클러스터 내 노드의 상태 표시:

`nomad node status`

- 작업 파일 유효성 검사:

`nomad job validate {{경로/대상/파일.nomad}}`

- 클러스터에서 실행할 작업 계획:

`nomad job plan {{경로/대상/파일.nomad}}`

- 클러스터에서 작업 실행:

`nomad job run {{경로/대상/파일.nomad}}`

- 현재 클러스터에서 실행 중인 작업의 상태 표시:

`nomad job status`

- 특정 작업에 대한 상세 상태 정보 표시:

`nomad job status {{작업_이름}}`

- 특정 할당의 로그를 지속적으로 팔로우:

`nomad alloc logs {{할당_id}}`

- 스토리지 볼륨의 상태 표시:

`nomad volume status`
