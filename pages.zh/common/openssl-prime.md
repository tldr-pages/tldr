# openssl prime

> OpenSSL 命令用于计算素数。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-prime.html>.

- 生成一个 2048 位的素数并以十六进制形式显示：

`openssl prime -generate -bits 2048 -hex`

- 检查给定的数字是否为素数：

`openssl prime {{number}}`
