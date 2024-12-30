# dbx

> 与 Databricks 平台交互。
> 注意：此工具已被退休，建议使用 Databricks 资产包。
> 更多信息：<https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>。

- 在当前工作目录中创建一个新的 `dbx` 项目：

`dbx configure --profile {{DEFAULT}}`

- 从指定路径同步本地文件到 DBFS 并监视更改：

`dbx sync dbfs --source {{path/to/directory}} --dest {{path/to/remote_directory}}`

- 将指定的工作流部署到工件存储：

`dbx deploy {{workflow_name}}`

- 在部署后启动指定的工作流：

`dbx launch {{workflow_name}}`