# kubectl exec

> 컨테이너 내부에서 명령 실행.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/>.

- 기본적으로 첫 번째 컨테이너에 접속하여 Bash 셸 실행:

`kubectl exec {{pod_이름}} {{[-it|--stdin --tty]}} -- bash`
