# cmctl

> 클러스터 내부의 cert-manager 리소스를 관리.
> 인증서 서명 상태를 확인하고, 요청을 승인/거부하고, 새 인증서 요청을 발급.
> 더 많은 정보: <https://cert-manager.io/docs/usage/cmctl/>.

- cert-manager API가 준비되었는지 확인:

`cmctl check api`

- 인증서 상태를 확인:

`cmctl status certificate {{인증서_이름}}`

- 기존 인증서를 기반으로 새 인증서 요청을 만듬:

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}}`

- 새 인증서 요청을 생성하고, 서명된 인증서를 가져오고, 최대 대기 시간을 설정:

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}} --fetch-certificate --timeout {{20m}}`
