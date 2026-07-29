# bd

> 用于 AI 编码代理的轻量级内存系统和 git 支持的问题跟踪器。
> 更多信息：<https://github.com/steveyegge/beads#usage>。

- 初始化项目数据库：

`bd init`

- 创建带有描述、优先级和类型的新问题：

`bd create {{问题标题}} {{[-d|--description]}} {{描述}} {{[-p|--priority]}} {{1}} {{[-t|--type]}} {{bug|feature|task|epic|chore}}`

- 列出所有问题：

`bd list`

- 显示准备处理的问题（无阻塞）：

`bd ready`

- 显示特定问题的详细信息：

`bd show {{问题_id}}`

- 更新问题状态：

`bd update {{问题_id}} {{[-s|--status]}} {{open|in_progress|blocked|closed}}`

- 手动同步更改并从 Git 导入最新内容：

`bd sync`

- 显示帮助：

`bd {{[-h|--help]}}`
