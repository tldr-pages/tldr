# kustomize

> 方便地部署 Kubernetes 资源。
> 更多信息：<https://github.com/kubernetes-sigs/kustomize>。

- 创建一个包含资源和命名空间的 kustomization 文件：

`kustomize create --resources {{deployment.yaml,service.yaml}} --namespace {{staging}}`

- 构建 kustomization 文件并使用 `kubectl` 部署：

`kustomize build . | kubectl apply -f -`

- 在 kustomization 文件中设置镜像：

`kustomize edit set image {{busybox=alpine:3.6}}`

- 搜索当前目录中的 Kubernetes 资源，以便添加到 kustomization 文件：

`kustomize create --autodetect`
