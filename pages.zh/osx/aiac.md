# aiac

> 使用 OpenAI 生成 IaC 配置、工具、查询等。
> 更多信息：<https://github.com/gofireflyio/aiac>.

- 为 Azure 存储帐户生成 Terraform 配置：

`aiac get terraform {{for an azure storage account}}`

- 为安全的 nginx 生成 Dockerfile：

`aiac get dockerfile {{for a secured nginx}}`

- 生成一个应用 Terraform 的 GitHub 动作：

`aiac get github action {{that plans and applies terraform}}`

- 生成一个 Python 端口扫描器：

`aiac get python {{code that scans all open ports in my network}}`

- 生成一个 MongoDB 查询：

`aiac get mongo {{query that aggregates all documents by created date}}`
