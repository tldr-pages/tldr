# openssl ts

> 生成和验证时间戳的 OpenSSL 命令。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-ts.html>.

- 生成特定文件的 SHA-512 时间戳请求，并输出到 `file.tsq`：

`openssl ts -query -data {{path/to/file}} -sha512 -out {{path/to/file.tsq}}`

- 检查特定时间戳响应文件的日期和元数据：

`openssl ts -reply -in {{path/to/file.tsr}} -text`

- 使用 SSL 证书文件验证时间戳请求文件和从服务器接收到的时间戳响应文件：

`openssl ts -verify -in {{path/to/file.tsr}} -queryfile {{path/to/file.tsq}} -partial_chain -CAfile {{path/to/cert.pem}}`

- 使用密钥和签名证书创建时间戳响应，并将其输出到 `file.tsr`：

`openssl ts -reply -queryfile {{path/to/file.tsq}} -inkey {{path/to/tsakey.pem}} -signer tsacert.pem -out {{path/to/file.tsr}}`
