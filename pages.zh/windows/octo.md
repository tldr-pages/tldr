# octo

> Octopus Deploy 的命令行工具。
> 更多信息：<https://octopus.com/docs/octopus-rest-api/octo.exe-command-line>。

- 创建包：

`octo pack --id={{package}}`

- 将包推送到 Octopus 服务器上的仓库：

`octo push --package={{package}}`

- 创建发布：

`octo create-release --project={{project_name}} --packageversion={{version}}`

- 部署发布：

`octo deploy-release --project={{project_name}} --packageversion={{version}} --deployto={{environment_name}} --tenant={{deployment_target}}`
