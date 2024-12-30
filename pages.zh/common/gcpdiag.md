# gcpdiag

> Google Cloud Platform 故障排除和诊断工具。
> 在 Docker 容器或 GCP Cloudshell 中运行。
> 更多信息：<https://github.com/GoogleCloudPlatform/gcpdiag>。

- 在您的项目上运行 `gcpdiag`，返回所有规则：

`gcpdiag lint --project={{gcp_project_id}}`

- 隐藏正常的规则：

`gcpdiag lint --project={{gcp_project_id}} --hide-ok`

- 使用服务账户私钥文件进行身份验证：

`gcpdiag lint --project={{gcp_project_id}} --auth-key {{path/to/private_key}}`

- 从几天前搜索日志和指标（默认：3天）：

`gcpdiag lint --project={{gcp_project_id}} --within-days {{number}}`

- 显示帮助信息：

`gcpdiag lint --help`