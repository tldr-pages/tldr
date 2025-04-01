# ern

> Electrode Native 平台命令行客户端。
> 更多信息：<https://native.electrode.io/reference/index-6>.

- 创建一个新的 `ern` 应用程序 (`MiniApp`)：

`ern create-miniapp {{application_name}}`

- 在 iOS/Android 运行器应用程序中运行一个或多个 `MiniApps`：

`ern run-{{ios|android}}`

- 创建一个 Electrode Native 容器：

`ern create-container --miniapps {{/path/to/miniapp_directory}} --platform {{ios|android}}`

- 将 Electrode Native 容器发布到本地 Maven 仓库：

`ern publish-container --publisher {{maven}} --platform {{android}} --extra {{'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'}}`

- 将 iOS 容器转换为预编译的二进制框架：

`ern transform-container --platform {{ios}} --transformer {{xcframework}}`

- 列出所有已安装的 Electrode Native 版本：

`ern platform versions`

- 设置日志级别：

`ern platform config set logLevel {{trace|debug}}`