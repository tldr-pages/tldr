# kubectl taint

> 노드에 taint 업데이트.
> 더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint>.

- 노드에 taint 적용:

`kubectl taint nodes {{노드_이름}} {{라벨_키}}={{라벨_값}}:{{효과}}`

- 노드에서 taint 제거:

`kubectl taint nodes {{노드_이름}} {{라벨_키}}:{{효과}}-`

- 노드에서 모든 taint 제거:

`kubectl taint nodes {{노드_이름}} {{라벨_키}}-`
