# rbenv

> 轻松安装 Ruby 版本并管理应用程序环境。
> 参见：`asdf`。
> 更多信息：<https://github.com/rbenv/rbenv>。

- 安装一个 Ruby 版本：

`rbenv install {{version}}`

- 显示每个 Ruby 的最新稳定版本列表：

`rbenv install --list`

- 显示已安装的 Ruby 版本列表：

`rbenv versions`

- 在整个系统中使用特定的 Ruby 版本：

`rbenv global {{version}}`

- 在应用程序/项目目录中使用特定的 Ruby 版本：

`rbenv local {{version}}`

- 显示当前选定的 Ruby 版本：

`rbenv version`

- 卸载一个 Ruby 版本：

`rbenv uninstall {{version}}`

- 显示包含指定可执行文件的所有 Ruby 版本：

`rbenv whence {{executable}}`
