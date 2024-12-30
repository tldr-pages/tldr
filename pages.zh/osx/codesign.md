# codesign

> 为 macOS 创建和操作代码签名。
> 更多信息：<https://keith.github.io/xcode-man-pages/codesign.1.html>。

- 使用证书对应用程序进行签名：

`codesign --sign "{{我的公司名称}}" {{path/to/application_file.app}}`

- 验证应用程序的证书：

`codesign --verify {{path/to/application_file.app}}`