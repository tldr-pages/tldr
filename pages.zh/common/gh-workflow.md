# gh 工作流

> 列出、查看和运行 GitHub Actions 工作流。
> 更多信息：<https://cli.github.com/manual/gh_workflow>。

- 交互式选择一个工作流以查看最新的作业：

`gh workflow view`

- 在默认浏览器中查看特定工作流：

`gh workflow view {{id|workflow_name|filename.yml}} --web`

- 显示特定工作流的 YAML 定义：

`gh workflow view {{id|workflow_name|filename.yml}} --yaml`

- 显示特定 Git 分支或标签的 YAML 定义：

`gh workflow view {{id|workflow_name|filename.yml}} --ref {{branch|tag_name}} --yaml`

- 列出工作流文件（使用 `--all` 包括禁用的工作流）：

`gh workflow list`

- 运行带有参数的手动工作流：

`gh workflow run {{id|workflow_name|filename.yml}} {{--raw-field param1=value1 --raw-field param2=value2 ...}}`

- 使用来自 `stdin` 的 JSON 参数，针对特定分支或标签运行手动工作流：

`echo '{{{"param1": "value1", "param2": "value2", ...}}}' | gh workflow run {{id|workflow_name|filename.yml}} --ref {{branch|tag_name}}`

- 启用或禁用特定工作流：

`gh workflow {{enable|disable}} {{id|workflow_name|filename.yml}}`