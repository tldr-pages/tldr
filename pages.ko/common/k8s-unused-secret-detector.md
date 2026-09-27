# k8s-unused-secret-detector

> 사용되지 않는 Kubernetes 시크릿 감지.
> 더 많은 정보: <https://github.com/dtan4/k8s-unused-secret-detector>.

- 사용되지 않는 시크릿 감지:

`k8s-unused-secret-detector`

- 특정 네임스페이스에서 사용되지 않는 시크릿 감지:

`k8s-unused-secret-detector {{[-n|--namespace]}} {{네임스페이스}}`

- 특정 네임스페이스에서 사용되지 않는 시크릿 삭제:

`k8s-unused-secret-detector {{[-n|--namespace]}} {{네임스페이스}} | kubectl delete secrets {{[-n|--namespace]}} {{네임스페이스}}`
