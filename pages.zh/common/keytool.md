# keytool

> 一个随 Java 一起提供的证书管理工具。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/keytool.html>.

- 创建一个密钥库：

`keytool -genkeypair -v -keystore {{path/to/file.keystore}} -alias {{key_name}}`

- 更改密钥库的密码：

`keytool -storepasswd -keystore {{path/to/file.keystore}}`

- 更改特定密钥库中密钥的密码：

`keytool -keypasswd -alias {{key_name}} -keystore {{path/to/file.keystore}}`
