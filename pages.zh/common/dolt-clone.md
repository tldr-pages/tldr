# dolt clone

> 克隆仓库到一个新的目录。
> 更多信息：<https://docs.dolthub.com/interfaces/cli#dolt-clone>.

- 克隆现有仓库到指定目录（默认为仓库名称）：

`dolt clone {{repository_url}} {{path/to/directory}}`

- 克隆现有仓库并添加一个特定的远程（默认为 origin）：

`dolt clone --remote {{remote_name}} {{repository_url}}`

- 只拉取特定分支（默认为所有分支）克隆现有仓库：

`dolt clone --branch {{branch_name}} {{repository_url}}`

- 使用 AWS 区域克隆仓库（如果未提供，则使用配置文件的默认区域）：

`dolt clone --aws-region {{region_name}} {{repository_url}}`

- 使用 AWS 凭证文件克隆仓库：

`dolt clone --aws-creds-file {{credentials_file}} {{repository_url}}`

- 使用 AWS 凭证配置文件克隆仓库（如果未提供，则使用默认配置文件）：

`dolt clone --aws-creds-profile {{profile_name}} {{repository_url}}`

- 使用 AWS 凭证类型克隆仓库：

`dolt clone --aws-creds-type {{credentials_type}} {{repository_url}}`
