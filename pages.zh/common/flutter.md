# flutter

> 谷歌的免费、开源和跨平台移动应用SDK。
> 一些子命令如 `pub` 有自己的使用文档。
> 更多信息：<https://github.com/flutter/flutter/wiki/The-flutter-tool>。

- 在同名目录中初始化一个新的Flutter项目：

`flutter create {{project_name}}`

- 检查所有外部工具是否正确安装：

`flutter doctor`

- 列出或更改Flutter频道：

`flutter channel {{stable|beta|dev|master}}`

- 在所有已启动的模拟器和连接的设备上运行Flutter：

`flutter run -d all`

- 从项目根目录在终端中运行测试：

`flutter test {{test/example_test.dart}}`

- 构建一个针对大多数现代智能手机的发布APK：

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`

- 显示有关特定命令的帮助：

`flutter help {{command}}`