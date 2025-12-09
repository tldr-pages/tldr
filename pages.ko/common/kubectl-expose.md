# kubectl expose

> 리소스를 새로운 Kubernetes 서비스로 노출.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_expose>.

- 컨테이너 포트에서 노드 포트로 제공될 리소스에 대한 서비스 생성:

`kubectl expose {{리소스_타입}} {{리소스_이름}} --port={{노드_포트}} --target-port={{컨테이너_포트}}`

- 파일로 식별된 리소스에 대한 서비스 생성:

`kubectl expose {{[-f|--filename]}} {{경로/대상/파일.yml}} --port={{노드_포트}} --target-port={{컨테이너_포트}}`

- 컨테이너 포트와 동일한 노드 포트로 제공할 이름이 있는 서비스 생성:

`kubectl expose {{리소스_타입}} {{리소스_이름}} --port={{노드_포트}} --name={{서비스_이름}}`
