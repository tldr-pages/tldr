# xcodebuild

> 构建 Xcode 项目。
> 更多信息：<https://developer.apple.com/library/archive/technotes/tn2339/_index.html>。

- 构建工作区：

`xcodebuild -workspace {{workspace_name.workspace}} -scheme {{scheme_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- 构建项目：

`xcodebuild -target {{target_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- 显示 SDK：

`xcodebuild -showsdks`