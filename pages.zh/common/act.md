# act

> 使用 Docker 在本地执行 GitHub Actions。
> 更多信息：<https://github.com/nektos/act>。

- [l] 列出可用的作业：

`act -l`

- 运行默认事件：

`act`

- 运行特定事件：

`act {{event_type}}`

- 运行特定的 [j]ob：

`act -j {{job_id}}`

- [n] 不实际运行操作（即干运行）：

`act -n`

- 显示 [v] 详细日志：

`act -v`

- 使用推送事件运行特定 [W]orkflow：

`act push -W {{path/to/workflow}}`