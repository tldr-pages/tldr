# gh workflow

> 列出、查看和运行 GitHub Actions 工作流。
> 更多信息：<https://cli.github.com/manual/gh_workflow>。

- 以交互式方式选择一个工作流以查看其最近的任务：

`gh workflow view`

- 在默认浏览器中查看指定的工作流：

`gh workflow view {{id|工作流名称|文件名.yml}} {{[-w|--web]}}`

- 显示指定工作流的 YAML 定义：

`gh workflow view {{id|工作流名称|文件名.yml}} {{[-y|--yaml]}}`

- 显示指定 Git 分支或标签下的 YAML 定义：

`gh workflow view {{id|工作流名称|文件名.yml}} {{[-r|--ref]}} {{分支|标签名}} {{[-y|--yaml]}}`

- 列出工作流文件（使用 `--all` 参数包含已被禁用的工作流）：

`gh workflow {{[ls|list]}}`

- 运行一个带参数的手动触发工作流：

`gh workflow run {{id|工作流名称|文件名.yml}} {{--raw-field 参数1=值1 --raw-field 参数2=值2 ...}}`

- 从 `stdin` 读取 JSON 参数，并在指定的分支或标签下运行手动工作流：

`echo '{{{"参数1": "值1", "参数2": "值2", ...}}}' | gh workflow run {{id|工作流名称|文件名.yml}} {{[-r|--ref]}} {{分支|标签名}}`

- 启用或禁用指定的工作流：

`gh workflow {{enable|disable}} {{id|工作流名称|文件名.yml}}`
