# kubectl certificate

> Kubernetes 인증서 서명 요청 관리.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/>.

- 이름으로 인증서 서명 요청 승인:

`kubectl certificate approve {{csr_이름}}`

- 이름으로 인증서 서명 요청 거부:

`kubectl certificate deny {{csr_이름}}`

- 매니페스트 파일에 정의된 인증서 서명 요청 승인:

`kubectl certificate approve --filename {{경로/대상/csr.yaml}}`

- 매니페스트 파일에 정의된 인증서 서명 요청 거부:

`kubectl certificate deny --filename {{경로/대상/csr.yaml}}`

- 이전에 거부된 인증서 서명 요청을 강제로 다시 승인:

`kubectl certificate approve --force {{csr_이름}}`
