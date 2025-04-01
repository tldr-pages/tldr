# dbx

> 与 Databricks 平台交互。
> 注意：此工具已退役，建议改用 Databricks Asset Bundles。
> 更多信息：<https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>。

- 在当前工作目录中创建一个新的 `dbx` 项目：

`dbx configure --profile {{DEFAULT}}`

- 从指定路径同步本地文件到 DBFS 并监视更改：

`dbx sync dbfs --source {{path/to/directory}} --dest {{path/to/remote_directory}}`

- 将指定的工作流部署到工件存储中：

`dbx deploy {{workflow_name}}`

- 部署后启动指定的工作流：

`dbx launch {{workflow_name}}`