# ern

> Electrode Native平台命令行客户端。
> 更多信息：<https://native.electrode.io/reference/index-6>。

- 创建一个新的 `ern` 应用程序（`MiniApp`）：

`ern create-miniapp {{application_name}}`

- 在iOS/Android Runner应用程序中运行一个或多个 `MiniApps`：

`ern run-{{ios|android}}`

- 创建一个Electrode Native容器：

`ern create-container --miniapps {{/path/to/miniapp_directory}} --platform {{ios|android}}`

- 将Electrode Native容器发布到本地Maven存储库：

`ern publish-container --publisher {{maven}} --platform {{android}} --extra {{'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'}}`

- 将iOS容器转换为预编译的二进制框架：

`ern transform-container --platform {{ios}} --transformer {{xcframework}}`

- 列出所有已安装的Electrode Native版本：

`ern platform versions`

- 设置日志级别：

`ern platform config set logLevel {{trace|debug}}`