# k8s-unused-secret-detector

> 检测未使用的 Kubernetes 密钥。
> 更多信息：<https://github.com/dtan4/k8s-unused-secret-detector>.

- 检测未使用的密钥：

`k8s-unused-secret-detector`

- 检测特定命名空间中的未使用密钥：

`k8s-unused-secret-detector -n {{namespace}}`

- 删除特定命名空间中的未使用密钥：

`k8s-unused-secret-detector -n {{namespace}} | kubectl delete secret -n {{namespace}}`
