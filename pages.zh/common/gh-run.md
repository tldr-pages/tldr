# gh run

> 查看、运行和监视最近的 GitHub Actions 工作流运行。
> 更多信息：<https://cli.github.com/manual/gh_run>。

- 交互式选择一个运行以查看有关作业的信息：

`gh run view`

- 显示特定运行的信息：

`gh run view {{workflow_run_number}}`

- 显示作业的步骤信息：

`gh run view --job={{job_number}}`

- 显示作业的日志：

`gh run view --job={{job_number}} --log`

- 检查特定工作流，如果运行失败则以非零状态退出：

`gh run view {{workflow_run_number}} --exit-status && {{echo "运行待处理或已通过"}}`

- 交互式选择一个活动运行并等待它完成：

`gh run watch`

- 显示一个运行的作业并等待它完成：

`gh run watch {{workflow_run_number}}`

- 重新运行特定工作流：

`gh run rerun {{workflow_run_number}}`