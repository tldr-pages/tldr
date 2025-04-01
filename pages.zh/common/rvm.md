# rvm

> 简单安装、管理和使用多个 Ruby 环境。
> 更多信息：<https://rvm.io>。

- 安装一个或多个版本的 Ruby：

`rvm install {{version1 version2 ...}}`

- 显示已安装的版本列表：

`rvm list`

- 使用特定版本的 Ruby：

`rvm use {{version}}`

- 设置默认的 Ruby 版本：

`rvm --default use {{version}}`

- 将一个版本的 Ruby 升级到新版本：

`rvm upgrade {{current_version}} {{new_version}}`

- 卸载一个版本的 Ruby 并保留其源代码：

`rvm uninstall {{version}}`

- 移除一个版本的 Ruby 及其源代码：

`rvm remove {{version}}`

- 显示适用于你操作系统的特定依赖项：

`rvm requirements`
