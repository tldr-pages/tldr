# xcodebuild

> 构建 Xcode 项目。

- 构建工作区：

`xcodebuild -workspace {{工作区名.工作区}} -scheme {{主题名}} -configuration {{配置名}} clean build SYMROOT={{SYMROOT_路径}}`

- 构建项目：

`xcodebuild -target {{目标名}} -configuration {{配置名}} clean build SYMROOT={{SYMROOT_路径}}`

- 显示 SDK：

`xcodebuild -showsdks`
