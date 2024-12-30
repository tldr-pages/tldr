# openssl req

> OpenSSL 命令用于管理 PKCS#10 证书签名请求。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-req.html>。

- 生成一个证书签名请求以发送到证书颁发机构：

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- 生成一个自签名证书及其相应的密钥对，并将两者存储在一个文件中：

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{filename.key}} -out {{filename.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`