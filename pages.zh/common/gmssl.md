# gmssl

> GmSSL 是一个支持 SM1、SM2、SM3、SM4、SM9 和 ZUC/ZUC256 的密码工具包。
> 更多信息：<http://gmssl.org/english.html>.

- 为文件生成 SM3 哈希值：

`gmssl sm3 {{path/to/file}}`

- 使用 SM4 加密算法加密文件：

`gmssl sms4 -e -in {{path/to/file}} -out {{path/to/file.sms4}}`

- 使用 SM4 加密算法解密文件：

`gmssl sms4 -d -in {{path/to/file.sms4}}`

- 生成 SM2 私钥：

`gmssl sm2 -genkey -out {{path/to/file.pem}}`

- 从现有私钥生成 SM2 公钥：

`gmssl sm2 -pubout -in {{path/to/file.pem}} -out {{path/to/file.pem.pub}}`

- 使用 ZUC 加密算法加密文件：

`gmssl zuc -e -in {{path/to/file}} -out {{path/to/file.zuc}}`

- 使用 ZUC 加密算法解密文件：

`gmssl zuc -d -in {{path/to/file.zuc}}`

- 显示版本信息：

`gmssl version`