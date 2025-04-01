# cosign

> 容器签名、验证和存储在 OCI 注册表中。
> 更多信息：<https://github.com/sigstore/cosign>。

- 生成密钥对：

`cosign generate-key-pair`

- 签名一个容器，并将签名存储在注册表中：

`cosign sign -key {{cosign.key}} {{image}}`

- 使用存储在 Kubernetes 密钥中的密钥对签名一个容器镜像：

`cosign sign -key k8s://{{namespace}}/{{key}} {{image}}`

- 使用本地密钥对文件签名：

`cosign sign-blob --key {{cosign.key}} {{path/to/file}}`

- 使用公钥验证容器：

`cosign verify -key {{cosign.pub}} {{image}}`

- 使用 Dockerfile 中的公钥验证镜像：

`cosign dockerfile verify -key {{cosign.pub}} {{path/to/Dockerfile}}`

- 使用存储在 Kubernetes 密钥中的公钥验证镜像：

`cosign verify -key k8s://{{namespace}}/{{key}} {{image}}`

- 复制容器镜像及其签名：

`cosign copy {{example.com/src:latest}} {{example.com/dest:latest}}`