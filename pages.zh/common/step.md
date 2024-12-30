# step

> 一个易于使用的命令行工具，用于构建、操作和自动化公钥基础设施（PKI）系统和工作流程。
> 另见：`openssl`。
> 更多信息：[https://smallstep.com/docs/step-cli/](https://smallstep.com/docs/step-cli/)。

- 检查证书的内容：

`step certificate inspect {{path/to/certificate.crt}}`

- 创建一个根CA证书和一个密钥（附加 `--no-password --insecure` 跳过私钥密码保护）：

`step certificate create "{{Example Root CA}}" {{path/to/root-ca.crt}} {{path/to/root-ca.key}} --profile root-ca`

- 为特定主机名生成证书并用根CA签名（生成CSR可以简化跳过）：

`step certificate create {{hostname.example.com}} {{path/to/hostname.crt}} {{path/to/hostname.key}} --profile leaf --ca {{path/to/root-ca.crt}} --ca-key {{path/to/root-ca.key}}`

- 验证证书链：

`step certificate verify {{path/to/hostname.crt}} --roots {{path/to/root-ca.crt}} --verbose`

- 将PEM格式的证书转换为DER并写入磁盘：

`step certificate format {{path/to/certificate.pem}} --out {{path/to/certificate.der}}`

- 在系统的默认信任库中安装或卸载根证书：

`step certificate {{install|uninstall}} {{path/to/root-ca.crt}}`

- 创建RSA/EC私钥和公钥对（附加 `--no-password --insecure` 跳过私钥密码保护）：

`step crypto keypair {{path/to/public_key}} {{path/to/private_key}} --kty {{RSA|EC}}`

- 显示子命令的帮助信息：

`step {{path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh}} --help`