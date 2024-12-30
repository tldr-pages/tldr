# todo.sh

> 一个简单且可扩展的 shell 脚本，用于管理你的 `todo.txt` 文件。
> 更多信息请访问：<https://github.com/todotxt/todo.txt-cli>。

- 列出每个项目：

`todo.sh ls`

- 添加一个带有项目和上下文标签的项目：

`todo.sh add '{{description}} +{{project}} @{{context}}'`

- 将项目标记为 [完成]：

`todo.sh do {{item_no}}`

- 移除一个项目：

`todo.sh rm {{item_no}}`

- 设置项目的 [优先级] (A-Z)：

`todo.sh pri {{item_no}} {{priority}}`

- 替换一个项目：

`todo.sh replace {{item_no}} '{{new_description}}'`