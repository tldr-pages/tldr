# mcfly

> 一个智能的命令历史搜索和管理工具。
> 替换默认的 shell 历史搜索（`<Ctrl r>`），提供带有上下文和相关性的智能搜索功能。
> 更多信息：<https://github.com/cantino/mcfly>。

- 打印指定 shell 的 mcfly 集成代码：

`mcfly init {{bash|fish|zsh}}`

- 搜索历史记录中的命令，显示 20 条结果：

`mcfly search --results {{20}} "{{search_terms}}"`

- 将新命令添加到历史记录中：

`mcfly add "{{command}}"`

- 记录目录已移动，并将历史记录从旧路径转移到新路径：

`mcfly move "{{path/to/old_directory}}" "{{path/to/new_directory}}"`

- 训练建议引擎（开发者工具）：

`mcfly train`

- 显示特定子命令的帮助信息：

`mcfly help {{subcommand}}`