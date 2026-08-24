# kubectl cordon

> 노드를 스케줄링 불가(unschedulable) 상태로 변경하여, 새로운 Pod가 배치되지 않도록 설정.
> 관련 항목: `kubectl uncordon`.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/>.

- 노드를 스케줄링 불가 상태로 설정:

`kubectl cordon {{노드_이름}}`

- 여러 노드를 스케줄링 불가 상태로 설정:

`kubectl cordon {{노드_이름1 노드_이름2 ...}}`

- 특정 컨텍스트에서 노드를 스케줄링 불가 상태로 설정:

`kubectl cordon {{노드_이름}} --context {{컨텍스트_이름}}`

- 라벨 선택자와 일치하는 노드들을 스케줄링 불가 상태로 설정:

`kubectl cordon {{[-l|--selector]}} {{라벨_키}}={{라벨_값}}`

- 실제 변경 없이 적용 결과만 미리 확인 (dry run):

`kubectl cordon {{노드_이름}} --dry-run={{none|server|client}}`
