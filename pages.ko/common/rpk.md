# rpk

> 하나의 실행 파일로 Redpanda 토픽, 클러스터, 그룹, 보안 등을 관리.
> 더 많은 정보: <https://docs.redpanda.com/current/reference/rpk/>.

- 새로운 토픽 생성:

`rpk topic create {{토픽_이름}}`

- 토픽에 메시지 전송:

`rpk topic produce {{토픽_이름}}`

- 여러 토픽의 메시지 소비:

`rpk topic consume {{토픽_이름1 토픽_이름2 ...}}`

- 모든 토픽 목록 표시:

`rpk topic list`

- 클러스터 정보 표시:

`rpk cluster info`

- 모든 컨슈머 그룹 목록 표시:

`rpk group list`

- 지연 정보를 포함하여 컨슈머 그룹 상세 정보 표시:

`rpk group describe {{그룹_이름}}`

- 버전 정보 표시:

`rpk version`
