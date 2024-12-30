# gitlab

> GitLab API 的 Ruby 封装。
> 一些子命令如 `ctl` 有自己的使用文档。
> 更多信息：<https://narkoz.github.io/gitlab/>.

- 创建一个新项目：

`gitlab create_project {{project_name}}`

- 获取特定提交的信息：

`gitlab commit {{project_name}} {{commit_hash}}`

- 获取 CI 流水线中的作业信息：

`gitlab pipeline_jobs {{project_name}} {{pipeline_id}}`

- 启动特定的 CI 作业：

`gitlab job_play {{project_name}} {{job_id}}`