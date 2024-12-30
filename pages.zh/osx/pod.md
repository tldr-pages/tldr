# pod

> Swift 和 Objective-C Cocoa 项目的依赖管理工具。
> 更多信息：<https://guides.cocoapods.org/terminal/commands.html>。

- 为当前项目创建一个默认内容的 Podfile：

`pod init`

- 下载并安装 Podfile 中定义的所有未安装的 pods：

`pod install`

- 列出所有可用的 pods：

`pod list`

- 显示当前安装的过时 pods：

`pod outdated`

- 将所有当前安装的 pods 更新到最新版本：

`pod update`

- 将特定（之前安装的）pod 更新到最新版本：

`pod update {{pod_name}}`

- 从 Xcode 项目中移除 CocoaPods：

`pod deintegrate {{xcode_project}}`