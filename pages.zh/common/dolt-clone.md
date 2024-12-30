# dolt clone

> 将一个仓库克隆到一个新目录中。
> 更多信息：<https://docs.dolthub.com/interfaces/cli#dolt-clone>。

- 将现有仓库克隆到指定目录（默认使用仓库名称）：

`dolt clone {{repository_url}} {{path/to/directory}}`

- 克隆现有仓库并添加特定远程（默认使用 origin）：

`dolt clone --remote {{remote_name}} {{repository_url}}`

- 仅克隆现有仓库的特定分支（默认克隆所有分支）：

`dolt clone --branch {{branch_name}} {{repository_url}}`

- 克隆一个仓库，使用 AWS 区域（如果未提供，则使用配置文件的默认区域）：

`dolt clone --aws-region {{region_name}} {{repository_url}}`

- 克隆一个仓库，使用 AWS 凭证文件：

`dolt clone --aws-creds-file {{credentials_file}} {{repository_url}}`

- 克隆一个仓库，使用 AWS 凭证配置文件（如果未提供，则使用默认配置文件）：

`dolt clone --aws-creds-profile {{profile_name}} {{repository_url}}`

- 克隆一个仓库，使用 AWS 凭证类型：

`dolt clone --aws-creds-type {{credentials_type}} {{repository_url}}`