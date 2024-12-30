# tod

> 一个用Rust编写的小型Todoist客户端。
> 它接受简单输入并将其放入您的收件箱或其他项目中。利用自然语言处理来分配截止日期、标签等。
> 更多信息：<https://github.com/alanvardy/tod>。

- 导入您的项目（这对于启用项目提示是必要的）：

`tod project import`

- 快速创建一个带截止日期的任务：

`tod --quickadd {{今天买更多牛奶}}`

- 创建一个新任务（系统会提示您输入内容和项目）：

`tod task create`

- 在项目中创建任务：

`tod task create --content "{{写更多rust}}" --project {{代码}}`

- 获取项目的下一个任务：

`tod task next`

- 获取您的工作日程：

`tod task list --scheduled --project {{工作}}`

- 获取所有工作任务：

`tod task list --project {{工作}}`