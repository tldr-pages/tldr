# kubectl logs

> 컨테이너의 로그를 조회하는 도구.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs>.

- 단일 컨테이너가 있는 파드의 로그 조회:

`kubectl logs {{포드_이름}}`

- 특정 컨테이너의 로그 조회:

`kubectl logs {{[-c|--container]}} {{컨테이너_이름}} {{포드_이름}}`

- 포드 내 모든 컨테이너의 로그 조회:

`kubectl logs --all-containers={{true}} {{포드_이름}}`

- 포드 로그 스트리밍:

`kubectl logs {{[-f|--follow]}} {{포드_이름}}`

- `10s`, `5m` 또는 `1h`와 같은 상대 시간 이후의 포드 로그 조회:

`kubectl logs --since {{상대_시간}} {{포드_이름}}`

- 가장 최근의 10개의 포드 로그 조회:

`kubectl logs --tail {{10}} {{포드_이름}}`

- 특정 배포의 모든 포드 로그 조회:

`kubectl logs {{[deploy|deployment]}}/{{배포_이름}}`
