# fly

> Concourse CI 的命令行工具。
> 更多信息：<https://concourse-ci.org/fly.html>.

- 认证并保存 Concourse 目标：

`fly --target {{target_name}} login --team-name {{team_name}} -c {{https://ci.example.com}}`

- 列出目标：

`fly targets`

- 列出管道：

`fly -t {{target_name}} pipelines`

- 上传或更新管道：

`fly -t {{target_name}} set-pipeline --config {{pipeline.yml}} --pipeline {{pipeline_name}}`

- 解锁管道：

`fly -t {{target_name}} unpause-pipeline --pipeline {{pipeline_name}}`

- 显示管道配置：

`fly -t {{target_name}} get-pipeline --pipeline {{pipeline_name}}`

- 更新本地的 fly 副本：

`fly -t {{target_name}} sync`

- 删除管道：

`fly -t {{target_name}} destroy-pipeline --pipeline {{pipeline_name}}`
