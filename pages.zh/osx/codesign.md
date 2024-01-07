# codesign

> 为 macOS 的应用程序签名。
> 更多信息：<https://www.unix.com/man-page/osx/1/codesign/>.

- 用证书签名：

`codesign --sign "{{公司名称}}" {{路径 / 应用名.app}}`

- 验证应用程序的签名：

`codesign --verify {{路径 / 应用名.app}}`
