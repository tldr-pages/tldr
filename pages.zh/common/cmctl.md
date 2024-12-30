# cmctl

> 管理集群中的 cert-manager 资源。
> 检查证书签署状态，批准/拒绝请求，并发起新的证书请求。
> 更多信息：<https://cert-manager.io/docs/usage/cmctl/>.

- 检查 cert-manager API 是否已就绪：

`cmctl check api`

- 检查证书的状态：

`cmctl status certificate {{cert_name}}`

- 基于现有证书创建新的证书请求：

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}}`

- 创建新的证书请求，获取签署的证书，并设置最大等待时间：

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}} --fetch-certificate --timeout {{20m}}`