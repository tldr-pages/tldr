# fluxctl

> Flux v1용 명령줄 도구.
> 더 많은 정보: <https://fluxcd.io/legacy/flux/references/fluxctl>.

- 특정 네임스페이스의 클러스터에서 현재 실행 중인 워크로드를 나열:

`fluxctl --k8s-fwd-ns={{네임스페이스}} list-workloads`

- 배포 및 사용 가능한 이미지 표시:

`fluxctl list-images`

- 클러스터를 Git 저장소와 동기화:

`fluxctl sync`

- 워크로드에 대한 자동 배포를 활성화:

`fluxctl automate`
