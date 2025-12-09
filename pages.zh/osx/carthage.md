# carthage

> Cocoa 应用程序的依赖性管理工具。
> 更多信息：<https://github.com/Carthage/Carthage>.

- 下载 Cartfile 中提到的所有依赖项的最新版本，并编译它们：

`carthage update`

- 仅针对 IOS 平台，升级依赖文件：

`carthage update --platform ios`

- 仅更新依赖，但不编译它们：

`carthage update --no-build`

- 下载并重新生成依赖项的当前版本（不更新它们）：

`carthage bootstrap`

- 重新编译特定依赖项：

`carthage build {{依赖包}}`
