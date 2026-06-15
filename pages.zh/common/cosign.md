# cosign

> 在 OCI 注册表中对容器进行签名、验证和存储。
> 更多信息：<https://github.com/sigstore/cosign/blob/main/doc/cosign.md>。

- 生成密钥对：

`cosign generate-key-pair`

- 对容器进行签名，并将签名存储在注册表中：

`cosign sign --key {{cosign.key}} {{镜像}}`

- 使用存储在 Kubernetes Secret 中的密钥对容器镜像进行签名：

`cosign sign --key k8s://{{命名空间}}/{{密钥}} {{镜像}}`

- 使用本地密钥对 blob 文件进行签名：

`cosign sign-blob --key {{cosign.key}} {{路径/到/文件}}`

- 使用公钥验证容器：

`cosign verify --key {{cosign.pub}} {{镜像}}`

- 使用 Dockerfile 中的公钥验证镜像：

`cosign dockerfile verify -key {{cosign.pub}} {{路径/到/Dockerfile}}`

- 使用存储在 Kubernetes Secret 中的公钥验证镜像：

`cosign verify --key k8s://{{命名空间}}/{{密钥}} {{镜像}}`

- 复制容器镜像及其签名：

`cosign copy {{example.com/src:latest}} {{example.com/dest:latest}}`
