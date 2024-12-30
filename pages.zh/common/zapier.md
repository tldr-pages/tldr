# zapier

> 创建、自动化和管理 zapier 集成。
> 一些子命令，如 `build`、`init`、`scaffold`、`push`、`test` 等，有自己的使用文档。
> 更多信息：<https://platform.zapier.com/reference/cli>。

- 连接到 Zapier 账户：

`zapier login`

- 使用项目模板初始化新的 Zapier 集成：

`zapier init {{path/to/directory}}`

- 向您的集成添加起始触发器、创建、搜索或资源：

`zapier scaffold {{trigger|create|search|resource}} {{name}}`

- 测试集成：

`zapier test`

- 构建并上传集成到 Zapier：

`zapier push`

- 显示帮助：

`zapier help`

- 显示特定命令的帮助：

`zapier help {{command}}`