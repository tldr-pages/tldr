# aiac

> 使用 OpenAI 生成基础设施即代码（IaC）配置、实用工具、查询等。
> 更多信息：<https://github.com/gofireflyio/aiac>。

- 生成用于 Azure 存储账户的 Terraform 配置：

`aiac get terraform {{用于 Azure 存储账户}}`

- 生成一个 `nginx` 的 Dockerfile：

`aiac get dockerfile {{用于安全的 nginx}}`

- 生成一个应用 Terraform 的 GitHub Actions 工作流：

`aiac get github action {{用于计划并应用 Terraform}}`

- 生成一个用 Python 编写的端口扫描器：

`aiac get python {{扫描我网络中所有开放端口的代码}}`

- 生成一个 MongoDB 查询：

`aiac get mongo {{按创建日期聚合所有文档的查询}}`
