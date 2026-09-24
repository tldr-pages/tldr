# kubectl wait

> Kubernetes 리소스가 특정 상태에 도달할 때까지 대기.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_wait/>.

- Deployment가 Available 상태가 될 때까지 대기:

`kubectl wait --for condition=available deployment/{{deployment_이름}}`

- 특정 라벨([l]abel)을 가진 모든 Pod가 Ready 상태가 될 때까지 대기:

`kubectl wait --for condition=ready {{[po|pods]}} {{[-l|--selector]}} {{라벨_키}}={{라벨_값}}`

- Pod가 삭제될 때까지 대기:

`kubectl wait --for delete {{[po|pods]}} {{pod_이름}}`

- Job이 완료될 때까지 최대 120초 동안 대기 (시간 내에 조건이 충족되지 않으면, 실패 상태 코드로 종료):

`kubectl wait --for condition=complete job/{{job_이름}} --timeout 120s`
