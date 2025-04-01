# tod

> 一个用 Rust 编写的轻量级 Todoist 客户端。
> 它接受简单的输入并将其添加到您的收件箱或另一个项目中。利用自然语言处理来分配截止日期、标签等。
> 更多信息：<https://github.com/alanvardy/tod>.

- 导入您的项目（这是启用项目提示所必需的）：

`tod project import`

- 快速创建带有截止日期的任务：

`tod --quickadd {{今天买更多牛奶}}`

- 创建新任务（您将被提示输入内容和项目）：

`tod task create`

- 在项目中创建任务：

`tod task create --content "{{更多地编写 Rust 代码}}" --project {{code}}`

- 获取项目的下一个任务：

`tod task next`

- 获取您的工作计划：

`tod task list --scheduled --project {{work}}`

- 获取工作中的所有任务：

`tod task list --project {{work}}`
