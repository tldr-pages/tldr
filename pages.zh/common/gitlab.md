# gitlab

> Ruby 语言的 GitLab API 封装。
> 一些子命令（如 `ctl`）有独立的使用文档。
> 更多信息：<https://narkoz.github.io/gitlab/>.

- 创建新项目：

`gitlab create_project {{project_name}}`

- 获取特定提交的信息：

`gitlab commit {{project_name}} {{commit_hash}}`

- 获取 CI 管道中的作业信息：

`gitlab pipeline_jobs {{project_name}} {{pipeline_id}}`

- 启动特定的 CI 作业：

`gitlab job_play {{project_name}} {{job_id}}`
