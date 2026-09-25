# kubectl attach

> 이미 실행중인 컨테이너 내부 프로세스에 연결.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_attach/>.

- Pod의 출력 확인:

`kubectl attach {{pod_이름}}`

- 지정한 Pod의 특정 컨테이너 출력 확인:

`kubectl attach {{pod_이름}} {{[-c|--container]}} {{컨테이너_이름}}`

- ReplicaSet의 첫 번째 Pod 출력 확인:

`kubectl attach {{[rs|replicaset]}}/{{replicaset_이름}}`

- Pod에 대화형 세션 연결:

`kubectl attach {{pod_이름}} {{[-it|--stdin --tty]}}`

- Pod의 특정 컨테이너에 대화형 세션 연결:

`kubectl attach {{pod_이름}} {{[-c|--container]}} {{컨테이너_이름}} {{[-it|--stdin --tty]}}`
