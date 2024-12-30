# mcfly

> 一款智能命令历史搜索和管理工具。
> 用一个智能搜索引擎替代默认的 shell 历史搜索（ctrl-r），为命令提供上下文和相关性。
> 更多信息请访问：<https://github.com/cantino/mcfly>。

- 打印指定 shell 的 mcfly 集成代码：

`mcfly init {{bash|fish|zsh}}`

- 在历史记录中搜索命令，返回 20 条结果：

`mcfly search --results {{20}} "{{search_terms}}"`

- 向历史记录中添加新命令：

`mcfly add "{{command}}"`

- 记录一个目录已移动，并将历史记录从旧路径转移到新路径：

`mcfly move "{{path/to/old_directory}}" "{{path/to/new_directory}}"`

- 训练建议引擎（开发者工具）：

`mcfly train`

- 显示特定子命令的帮助：

`mcfly help {{subcommand}}`