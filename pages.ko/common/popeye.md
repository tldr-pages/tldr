# popeye

> Kubernetes 배포 매니페스트의 잠재적 문제 보고.
> 더 많은 정보: <https://github.com/derailed/popeye>.

- 현재 Kubernetes 클러스터 스캔:

`popeye`

- 특정 네임스페이스 스캔:

`popeye -n {{네임스페이스}}`

- 특정 Kubernetes 컨텍스트 스캔:

`popeye --context={{컨텍스트}}`

- 스캐닝에 스피니치 구성 파일 사용:

`popeye -f {{spinach.yaml}}`
