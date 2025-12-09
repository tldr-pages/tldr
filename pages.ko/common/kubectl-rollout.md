# kubectl rollout

> Kubernetes 리소스(배포, 데몬셋, 스테이트풀셋)의 롤아웃 관리.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout>.

- 리소스의 롤링 재시작 시작:

`kubectl rollout restart {{리소스_유형}}/{{리소스_이름}}`

- 리소스의 롤링 업데이트 상태 보기:

`kubectl rollout status {{리소스_유형}}/{{리소스_이름}}`

- 리소스를 이전 리비전으로 롤백:

`kubectl rollout undo {{리소스_유형}}/{{리소스_이름}}`

- 리소스의 롤아웃 기록 보기:

`kubectl rollout history {{리소스_유형}}/{{리소스_이름}}`
