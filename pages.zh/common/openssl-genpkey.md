# openssl genpkey

> OpenSSL 命令用于生成非对称密钥对。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html>.

- 生成 2048 位的 RSA 私钥，并将其保存到指定文件：

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{filename.key}}`

- 生成使用 `prime256v1` 曲线的椭圆曲线私钥，并将其保存到指定文件：

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{filename.key}}`

- 生成 `ED25519` 椭圆曲线私钥，并将其保存到指定文件：

`openssl genpkey -algorithm {{ED25519}} -out {{filename.key}}`