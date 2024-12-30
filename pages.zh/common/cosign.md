# cosign

> 在OCI注册表中进行容器签名、验证和存储。
> 更多信息：<https://github.com/sigstore/cosign>。

- 生成密钥对：

`cosign generate-key-pair`

- 签名一个容器并将签名存储在注册表中：

`cosign sign -key {{cosign.key}} {{image}}`

- 使用存储在Kubernetes密钥中的密钥对签名一个容器镜像：

`cosign sign -key k8s://{{namespace}}/{{key}} {{image}}`

- 使用本地密钥对文件签名一个blob：

`cosign sign-blob --key {{cosign.key}} {{path/to/file}}`

- 使用公钥验证一个容器：

`cosign verify -key {{cosign.pub}} {{image}}`

- 在Dockerfile中使用公钥验证镜像：

`cosign dockerfile verify -key {{cosign.pub}} {{path/to/Dockerfile}}`

- 使用存储在Kubernetes密钥中的公钥验证一个镜像：

`cosign verify -key k8s://{{namespace}}/{{key}} {{image}}`

- 复制一个容器镜像及其签名：

`cosign copy {{example.com/src:latest}} {{example.com/dest:latest}}`