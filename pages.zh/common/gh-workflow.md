# gh workflow

> 列出、查看和运行 GitHub Actions 工作流。
> 更多信息：<https://cli.github.com/manual/gh_workflow>.

- 交互式选择一个工作流以查看其最新的作业：

`gh workflow view`

- 在默认浏览器中查看特定工作流：

`gh workflow view {{id|workflow_name|filename.yml}} --web`

- 显示特定工作流的 YAML 定义：

`gh workflow view {{id|workflow_name|filename.yml}} --yaml`

- 显示特定 Git 分支或标签的 YAML 定义：

`gh workflow view {{id|workflow_name|filename.yml}} --ref {{branch|tag_name}} --yaml`

- 列出工作流文件（使用 `--all` 包括已禁用的工作流）：

`gh workflow list`

- 使用参数运行手动工作流：

`gh workflow run {{id|workflow_name|filename.yml}} {{--raw-field param1=value1 --raw-field param2=value2 ...}}`

- 使用特定分支或标签，并从 `stdin` 传递 JSON 参数运行手动工作流：

`echo '{{{"param1": "value1", "param2": "value2", ...}}}' | gh workflow run {{id|workflow_name|filename.yml}} --ref {{branch|tag_name}}`

- 启用或禁用特定工作流：

`gh workflow {{enable|disable}} {{id|workflow_name|filename.yml}}`