# fvm

> Flutter 版本管理器。
> 更多信息：<https://fvm.app/documentation/guides/basic-commands>。

- 安装一个版本的 Flutter SDK。对于项目设置，请勿使用 `version`：

`fvm install {{version}}`

- 在项目中设置特定版本的 Flutter SDK：

`fvm use {{version}} {{options}}`

- 设置 Flutter SDK 的全局版本：

`fvm global {{version}}`

- 删除 FVM 缓存：

`fvm destroy`

- 移除特定版本的 Flutter SDK：

`fvm remove {{version}}`

- 列出所有已安装的 Flutter SDK 版本：

`fvm list`

- 列出所有 Flutter SDK 发布版本：

`fvm releases`