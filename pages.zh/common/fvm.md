# fvm

> Flutter 版本管理工具。
> 更多信息：<https://fvm.app/documentation/guides/basic-commands>。

- 安装 Flutter SDK 的某个版本。不带 `version` 参数时用于项目设置：

`fvm install {{version}}`

- 在项目中设置 Flutter SDK 的特定版本：

`fvm use {{version}} {{options}}`

- 设置 Flutter SDK 的全局版本：

`fvm global {{version}}`

- 删除 FVM 缓存：

`fvm destroy`

- 移除 Flutter SDK 的特定版本：

`fvm remove {{version}}`

- 列出所有已安装的 Flutter SDK 版本：

`fvm list`

- 列出所有 Flutter SDK 的发行版本：

`fvm releases`