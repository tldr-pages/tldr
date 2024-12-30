# Carthage

> 一个用于Cocoa应用程序的依赖管理工具。
> 更多信息：<https://github.com/Carthage/Carthage>。

- 下载Cartfile中提到的所有依赖的最新版本，并构建它们：

`carthage update`

- 更新依赖，但仅为iOS构建：

`carthage update --platform ios`

- 更新依赖，但不构建任何依赖：

`carthage update --no-build`

- 下载并重建当前版本的依赖（不更新它们）：

`carthage bootstrap`

- 重建特定的依赖：

`carthage build {{dependency}}`