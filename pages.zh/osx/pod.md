# pod

> Swift 和 Objective-C Cocoa 项目的依赖关系管理。

- 为当前项目初始化包含默认内容的 podfile：

`pod init`

- 下载并安装 pod 文件中定义的所有 pod（以前未安装）：

`pod install`

- 列出所有可用的 pod：

`pod list`

- 显示过时的 pod（当前安装的 pod）：

`pod outdated`

- 将当前安装的所有 pod 更新到其最新版本：

`pod update`

- 将特定（以前安装的）pod 更新为其最新版本：

`pod update {{pod_名}}`

- 从 Xcode 项目中删除 CocoaPods：

`pod deintegrate {{xcode_项目}}`
