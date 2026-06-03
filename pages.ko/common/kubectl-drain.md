# kubectl drain

> 유지보수를 하기 위해 노드를 스케줄링 불가(unschedulable) 상태로 만들고 모든 Pod를 내보냄(evict).
> 관련 항목: `kubectl cordon`, `kubectl uncordon`.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/>.

- 노드 드레인 수행:

`kubectl drain {{노드_이름}}`

- DaemonSet이 관리하는 Pod를 무시하고 노드 드레인 수행:

`kubectl drain {{노드_이름}} --ignore-daemonsets`

- emptyDir 볼륨을 사용하는 Pod를 삭제하면서 노드 드레인 수행 (로컬 데이터 손실 가능):

`kubectl drain {{노드_이름}} --ignore-daemonsets --delete-emptydir-data`

- 컨트롤러가 관리하지 않는 Pod도 강제로 내보내면서 노드 드레인 수행:

`kubectl drain {{노드_이름}} --force`

- Pod 종료를 위해 사용자 지정 유예 시간을 설정:

`kubectl drain {{노드_이름}} --grace-period {{초}}`

- 특정 라벨 선택자에 일치하는 Pod만 내보내며 노드 드레인 수행:

`kubectl drain {{노드_이름}} --pod-selector {{라벨_키}}={{라벨_값}}`

- 타임아웃을 지정해 노드 드레인 수행:

`kubectl drain {{노드_이름}} --timeout {{기간}}`

- 실제 Pod 내보내기 없이 드레인 결과를 미리 확인 (dry run):

`kubectl drain {{노드_이름}} --dry-run={{none|server|client}}`
