# sdk

> 管理多个软件开发工具包的并行版本。
> 支持 Java、Groovy、Scala、Kotlin、Gradle、Maven、Vert.x 等多种语言。
> 更多信息：<https://sdkman.io/usage>。

- 安装一个 SDK 版本：

`sdk install {{sdk_name}} {{sdk_version}}`

- 在当前终端会话中使用特定的 SDK 版本：

`sdk use {{sdk_name}} {{sdk_version}}`

- 显示任何可用 SDK 的稳定版本：

`sdk current {{sdk_name}}`

- 显示所有已安装 SDK 的稳定版本：

`sdk current`

- 列出所有可用的 SDK：

`sdk list`

- 列出一个 SDK 的所有版本：

`sdk list {{sdk_name}}`

- 将 SDK 升级到最新的稳定版本：

`sdk upgrade {{sdk_name}}`

- 卸载特定的 SDK 版本：

`sdk rm {{sdk_name}} {{sdk_version}}`