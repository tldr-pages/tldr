# kubectl scale

> 배포, 레플리카 세트, 복제 컨트롤러 또는 스테이트풀 세트의 크기를 조정.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_scale>.

- 레플리카 세트 크기 조정:

`kubectl scale --replicas={{레플리카_수}} rs/{{레플리카_이름}}`

- 파일로 식별된 리소스 크기 조정:

`kubectl scale --replicas={{레플리카_수}} {{[-f|--filename]}} {{경로/대상/파일.yml}}`

- 현재 레플리카 수를 기준으로 배포 크기 조정:

`kubectl scale --current-replicas={{현재_레플리카_수}} --replicas={{레플리카_수}} deployment/{{배포_이름}}`
