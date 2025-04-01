# openssl genrsa

> 生成 RSA 私钥的 OpenSSL 命令。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-genrsa.html>.

- 生成 2048 位的 RSA 私钥并输出到 `stdout`:

`openssl genrsa`

- 将任意位数的 RSA 私钥保存到输出文件中:

`openssl genrsa -out {{output_file.key}} {{1234}}`

- 生成 RSA 私钥并使用 AES256 加密（需要输入密码）:

`openssl genrsa {{-aes256}}`