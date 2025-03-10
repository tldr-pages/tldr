# zapier scaffold

> 添加一个起始 {触发器}、{创建}、{搜索} 或 {资源} 到一个集成。
> 更多信息：<https://platform.zapier.com/reference/cli#scaffold>.

- 创建一个新的触发器、创建、搜索或资源：

`zapier scaffold {{trigger|search|create|resource}} {{名称}}`

- 为生成的文件指定一个自定义目标目录：

`zapier scaffold {{trigger|search|create|resource}} {{名称}} {{[-d|--dest]}}={{路径/到/目录}}`

- 在生成文件时覆盖已有文件：

`zapier scaffold {{trigger|search|create|resource}} {{名称}} {{[-f|--force]}}`

- 从生成的文件中排除注释：

`zapier scaffold {{trigger|search|create|resource}} {{名称}} --no-help`

- 显示额外的调试输出：

`zapier scaffold {{[-d|--debug]}}`
