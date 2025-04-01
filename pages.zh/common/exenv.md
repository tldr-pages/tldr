# exenv

> 轻松安装 Elixir 版本并管理应用程序环境。
> 更多信息：<https://github.com/mururu/exenv>。

- 显示已安装的版本列表：

`exenv versions`

- 为整个系统使用特定版本的 Elixir：

`exenv global {{version}}`

- 为当前应用程序/项目目录使用特定版本的 Elixir：

`exenv local {{version}}`

- 显示当前选择的 Elixir 版本：

`exenv {{version}}`

- 安装 Elixir 版本（需要 `elixir-build` 插件 <https://github.com/mururu/elixir-build>）：

`exenv install {{version}}`