# aiac

> 使用 OpenAI 生成基础设施即代码（IaC）配置、工具、查询等。
> 更多信息：<https://github.com/gofireflyio/aiac>。

- 为 Azure 存储账户生成 Terraform：

`aiac get terraform {{为一个 Azure 存储账户}}`

- 为 nginx 生成 Dockerfile：

`aiac get dockerfile {{为一个安全的 nginx}}`

- 生成一个应用 Terraform 的 GitHub 操作：

`aiac get github action {{计划并应用 terraform}}`

- 在 Python 中生成一个端口扫描器：

`aiac get python {{扫描我网络中所有开放端口的代码}}`

- 生成一个 MongoDB 查询：

`aiac get mongo {{按创建日期聚合所有文档的查询}}`