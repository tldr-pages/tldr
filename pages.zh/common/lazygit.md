# lazygit

> 一个简单的 Git 命令终端用户界面，提供一个直观的接口来管理仓库。
> 更多信息：<https://github.com/jesseduffield/lazygit>。

- 在当前仓库中打开 Lazygit：

`lazygit`

- 打开指定 Git 仓库的 Lazygit：

`lazygit --path {{path/to/repository}}`

- 启动 Lazygit 并聚焦于特定面板：

`lazygit {{status|branch|log|stash|...}}`

- 打印默认的 Lazygit 配置：

`lazygit --config`

- 追踪 Lazygit 日志（在另一个终端中使用调试模式时非常有用）：

`lazygit --logs`

- 以调试模式运行 Lazygit：

`lazygit --debug`

- 打印配置目录：

`lazygit --print-config-dir`