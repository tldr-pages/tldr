# sattach

> 附加到 Slurm 作业步骤。
> 更多信息：<https://slurm.schedmd.com/sattach.html>.

- 将 Slurm 作业步骤的 IO 流（`stdout`、`stderr` 和 `stdin`）重定向到当前终端：

`sattach {{jobid}}.{{stepid}}`

- 使用当前控制台的输入作为指定任务的 `stdin`：

`sattach --input-filter {{task_number}}`

- 仅重定向指定任务的 `stdin`/`stderr`：

`sattach --{{output|error}}-filter {{task_number}}`