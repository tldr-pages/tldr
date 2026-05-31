# kubectl annotate

> Kubernetes 리소스에 annotation 추가 및 관리.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/>.

- Pod에 annotation 추가:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{키}}={{값}}`

- 기존 annotation 값을 덮어씌워 업데이트:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{키}}={{값}} --overwrite`

- 특정 라벨 선택자와 일치하는 네임스페이스 내 모든 Pod에 annotation 추가:

`kubectl annotate {{[po|pods]}} {{키}}={{값}} {{[-l|--selector]}} {{라벨_키}}={{라벨_값}}`

- Pod에 설정된 모든 annotation 목록 표시:

`kubectl annotate {{[po|pods]}} {{pod_이름}} --list`

- Pod에서 annotation 제거:

`kubectl annotate {{[po|pods]}} {{pod_이름}} {{키}}-`
