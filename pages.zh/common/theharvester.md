# theHarvester

> 一款旨在渗透测试早期阶段使用的工具。
> 更多信息：<https://github.com/laramies/theHarvester>。

- 使用 Google 收集域信息：

`theHarvester --domain {{domain_name}} --source google`

- 使用多个来源收集域信息：

`theHarvester --domain {{domain_name}} --source {{duckduckgo,bing,crtsh}}`

- 更改结果限制：

`theHarvester --domain {{domain_name}} --source {{google}} --limit {{200}}`

- 将输出保存为 XML 和 HTML 格式的两个文件：

`theHarvester --domain {{domain_name}} --source {{google}} --file {{output_file_name}}`

- 显示帮助信息：

`theHarvester --help`