# zapier 脚手架

> 添加一个起始触发器、创建、搜索或资源到集成中。
> 更多信息：<https://platform.zapier.com/reference/cli#scaffold>。

- 脚手架一个新的触发器、创建、搜索或资源：

`zapier scaffold {{trigger|search|create|resource}} {{noun}}`

- 指定脚手架文件的自定义目标目录：

`zapier scaffold {{trigger|search|create|resource}} {{noun}} {{-d|--dest}}={{path/to/directory}}`

- 在脚手架时覆盖现有文件：

`zapier scaffold {{trigger|search|create|resource}} {{noun}} {{-f|--force}}`

- 从脚手架文件中排除注释：

`zapier scaffold {{trigger|search|create|resource}} {{noun}} --no-help`

- 显示额外的调试输出：

`zapier scaffold {{-d|--debug}}`