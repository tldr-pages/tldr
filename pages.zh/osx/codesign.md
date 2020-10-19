# codesign

> 为 macOS 的应用程序签名.

- 用证书签名:

`codesign -s "{{公司名称}}" {{路径 / 应用名.app}}`

- 验证应用程序的签名:

`codesign -v {{路径 / 应用名.app}}`
