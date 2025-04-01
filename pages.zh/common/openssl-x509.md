# openssl x509

> OpenSSL 命令用于管理 X.509 证书。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- 显示证书信息：

`openssl x509 -in {{filename.crt}} -noout -text`

- 显示证书的过期日期：

`openssl x509 -enddate -noout -in {{filename.pem}}`

- 在二进制 DER 编码和文本 PEM 编码之间转换证书：

`openssl x509 -inform {{der}} -outform {{pem}} -in {{original_certificate_file}} -out {{converted_certificate_file}}`

- 将证书的公钥存储在文件中：

`openssl x509 -in {{certificate_file}} -noout -pubkey -out {{output_file}}`