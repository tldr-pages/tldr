# gh run

> 查看、运行和监视最近的 GitHub Actions 工作流运行。
> 更多信息：<https://cli.github.com/manual/gh_run>.

- 交互式选择一个运行以查看其作业信息：

`gh run view`

- 显示特定运行的信息：

`gh run view {{workflow_run_number}}`

- 显示作业的步骤信息：

`gh run view --job={{job_number}}`

- 显示作业的日志：

`gh run view --job={{job_number}} --log`

- 检查特定工作流并在运行失败时退出并返回非零状态：

`gh run view {{workflow_run_number}} --exit-status && {{echo "运行挂起或通过"}}`

- 交互式选择一个活动运行并等待其完成：

`gh run watch`

- 显示运行的作业并等待其完成：

`gh run watch {{workflow_run_number}}`

- 重新运行特定的工作流：

`gh run rerun {{workflow_run_number}}`