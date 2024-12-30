# xctool

> 构建 Xcode 项目。
> 更多信息：<https://github.com/facebookarchive/xctool>。

- 在没有任何工作区的情况下构建单个项目：

`xctool -project {{YourProject.xcodeproj}} -scheme {{YourScheme}} build`

- 构建作为工作区一部分的项目：

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} build`

- 清理、构建并执行所有测试：

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} clean build test`