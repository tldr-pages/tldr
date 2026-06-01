# lazygit

> Git 命令的简易终端界面，提供管理仓库的直观操作。
> 更多信息：<https://manned.org/lazygit>。

- 在当前仓库中打开 Lazygit：

lazygit

- 打开指定 Git 仓库的 Lazygit：

lazygit {{[-p|--path]}} {{仓库/路径}}

- 聚焦到指定面板启动 Lazygit：

lazygit {{status|branch|log|stash|...}}

- 打印默认 Lazygit 配置：

lazygit {{[-c|--config]}}

- 输出 Lazygit 日志（与另一个终端中的调试模式配合使用）：

lazygit {{[-l|--logs]}}

- 以调试模式运行 Lazygit：

lazygit {{[-d|--debug]}}

- 打印配置目录路径：

lazygit {{[-cd|--print-config-dir]}}
