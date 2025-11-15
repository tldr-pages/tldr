# kubectl edit

> Kubernetes 리소스를 편집.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit>.

- Pod 편집:

`kubectl edit pod/{{pod_이름}}`

- Deployment 편집:

`kubectl edit deployment/{{deployment_이름}}`

- Service 편집:

`kubectl edit svc/{{service_이름}}`

- 특정 편집기를 사용하여 리소스 편집:

`KUBE_EDITOR={{nano}} kubectl edit {{resource}}/{{리소스_이름}}`

- JSON 형식으로 리소스 편집:

`kubectl edit {{resource}}/{{리소스_이름}} --output json`
