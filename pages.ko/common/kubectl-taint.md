# kubectl taint

> 노드에 taint 업데이트.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_taint>.

- 노드에 taint 적용:

`kubectl taint {{[no|nodes]}} {{노드_이름}} {{라벨_키}}={{라벨_값}}:{{효과}}`

- 노드에서 taint 제거:

`kubectl taint {{[no|nodes]}} {{노드_이름}} {{라벨_키}}:{{효과}}-`

- 노드에서 모든 taint 제거:

`kubectl taint {{[no|nodes]}} {{노드_이름}} {{라벨_키}}-`
