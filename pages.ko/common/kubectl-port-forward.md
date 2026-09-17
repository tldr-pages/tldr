# kubectl port-forward

> 하나 이상의 로컬 포트를 local ports to a pod.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/>.

- 로컬 포트 5000, 6000을 Pod의 5000, 6000 포트로 포워딩:

`kubectl port-forward {{[po|pods]}}/{{pod_이름}} 5000 6000`

- 임의의 로컬 포트를 Pod의 5000 포트로 포워딩:

`kubectl port-forward {{[po|pods]}}/{{pod_이름}} :5000`

- 로컬 포트 5000, 6000을 Deployment의 5000, 6000 포트로 포워딩:

`kubectl port-forward {{[deploy|deployment]}}/{{deployment_이름}} 5000 6000`

- 로컬 포트 8443을 Service의 https 포트로 포워딩:

`kubectl port-forward {{[svc|service]}}/{{서비스_이름}} 8443:https`

- 모든 네트워크 인터페이스에서 8888 포트를 Pod의 5000 포트로 포워딩:

`kubectl port-forward {{[po|pods]}}/{{pod_이름}} 8888:5000 --address 0.0.0.0`

- localhost와 특정 IP에서 8888 포트를 Pod의 5000 포트로 포워딩:

`kubectl port-forward {{[po|pods]}}/{{pod_이름}} 8888:5000 --address localhost,{{10.19.21.23}}`
