# gmssl

> GmSSL是一个加密工具包，支持SM1、SM2、SM3、SM4、SM9和ZUC/ZUC256。
> 更多信息：<http://gmssl.org/english.html>。

- 为文件生成SM3哈希：

`gmssl sm3 {{path/to/file}}`

- 使用SM4密码加密文件：

`gmssl sms4 -e -in {{path/to/file}} -out {{path/to/file.sms4}}`

- 使用SM4密码解密文件：

`gmssl sms4 -d -in {{path/to/file.sms4}}`

- 生成SM2私钥：

`gmssl sm2 -genkey -out {{path/to/file.pem}}`

- 从现有私钥生成SM2公钥：

`gmssl sm2 -pubout -in {{path/to/file.pem}} -out {{path/to/file.pem.pub}}`

- 使用ZUC密码加密文件：

`gmssl zuc -e -in {{path/to/file}} -out {{path/to/file.zuc}}`

- 使用ZUC密码解密文件：

`gmssl zuc -d -in {{path/to/file.zuc}}`

- 显示版本：

`gmssl version`