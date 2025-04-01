# step

> 一个易于使用的 CLI 工具，用于构建、操作和自动化公钥基础设施（PKI）系统和工作流程。
> 参见: `openssl`。
> 更多信息: <https://smallstep.com/docs/step-cli/>。

- 查看证书的内容：

`step certificate inspect {{path/to/certificate.crt}}`

- 创建一个根 CA 证书和密钥（附加 `--no-password --insecure` 以跳过私钥密码保护）：

`step certificate create "{{Example Root CA}}" {{path/to/root-ca.crt}} {{path/to/root-ca.key}} --profile root-ca`

- 为特定主机名生成证书并用根 CA 签名（生成 CSR 可以省略以简化过程）：

`step certificate create {{hostname.example.com}} {{path/to/hostname.crt}} {{path/to/hostname.key}} --profile leaf --ca {{path/to/root-ca.crt}} --ca-key {{path/to/root-ca.key}}`

- 验证证书链：

`step certificate verify {{path/to/hostname.crt}} --roots {{path/to/root-ca.crt}} --verbose`

- 将 PEM 格式的证书转换为 DER 格式并写入磁盘：

`step certificate format {{path/to/certificate.pem}} --out {{path/to/certificate.der}}`

- 在系统默认的信任存储中安装或卸载根证书：

`step certificate {{install|uninstall}} {{path/to/root-ca.crt}}`

- 创建一个 RSA/EC 私钥和公钥对（附加 `--no-password --insecure` 以跳过私钥密码保护）：

`step crypto keypair {{path/to/public_key}} {{path/to/private_key}} --kty {{RSA|EC}}`

- 显示子命令的帮助：

`step {{path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh}} --help`
