# openssl genrsa

> OpenSSL命令用于生成RSA私钥。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-genrsa.html>。

- 生成一个2048位的RSA私钥并输出到`stdout`：

`openssl genrsa`

- 将一个任意位数的RSA私钥保存到输出文件：

`openssl genrsa -out {{output_file.key}} {{1234}}`

- 生成一个RSA私钥并使用AES256加密（您将被要求输入密码短语）：

`openssl genrsa {{-aes256}}`