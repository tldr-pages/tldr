# kubeseal

> 用于使用 Bitnami Sealed Secrets 控制器在客户端加密 Kubernetes 密钥的工具。
> 生成的 SealedSecret 资源可以安全地存储在版本控制系统中。
> 需要在集群中运行一个控制器（例如，通过 `kubectl apply -f controller.yaml` 安装）。
> 更多信息：<https://github.com/bitnami-labs/sealed-secrets>.

- 从 YAML 文件加密 Kubernetes 密钥为 SealedSecret（默认 JSON 输出）：

`kubeseal < {{secret.yaml}} > {{sealedsecret.json}}`

- 使用 API 认证的令牌加密密钥，并以 YAML 或 JSON 格式输出：

`kubeseal {{[-o|--format]}} {{yaml|json}} --token {{my-bearer-token}} < {{secret.yaml}} > {{sealedsecret.yaml}}`

- 使用指定的 SealedSecrets 控制器命名空间和名称加密密钥：

`kubeseal --controller-namespace {{controller-namespace}} --controller-name {{controller-name}} < {{secret.yaml}} > {{sealedsecret.yaml}}`

- 从文件中加密原始密钥值，指定名称和范围：

`kubeseal --raw --from-file {{path/to/secret.txt}} --name {{my-secret}} --scope {{strict|namespace-wide|cluster-wide}} > {{sealedsecret.yaml}}`

- 使用基本认证获取控制器的公钥证书以进行离线加密：

`kubeseal --fetch-cert --username {{username}} --password {{password}} > {{cert.pem}}`

- 使用获取到的证书离线加密密钥：

`kubeseal --cert {{cert.pem}} < {{secret.yaml}} > {{sealedsecret.yaml}}`

- 将密钥合并到现有的 SealedSecret 文件中：

`kubeseal --merge-into {{sealedsecret.yaml}} < {{secret.yaml}}`

- 验证 SealedSecret 而不进行应用：

`kubeseal --validate < {{sealedsecret.yaml}}`