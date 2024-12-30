# aws route53

> AWS Route53 的命令行工具 - Route 53 是一个高可用和可扩展的域名系统（DNS）网络服务。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>。

- 列出所有托管区域，包括私有和公共区域：

`aws route53 list-hosted-zones`

- 显示某个区域中的所有记录：

`aws route53 list-resource-record-sets --hosted-zone-id {{zone_id}}`

- 使用请求标识符安全地重试操作以创建一个新的公共区域：

`aws route53 create-hosted-zone --name {{name}} --caller-reference {{request_identifier}}`

- 删除一个区域（如果该区域有非默认的 SOA 和 NS 记录，此命令将失败）：

`aws route53 delete-hosted-zone --id {{zone_id}}`

- 测试给定区域的 Amazon 服务器的 DNS 解析：

`aws route53 test-dns-answer --hosted-zone-id {{zone_id}} --record-name {{name}} --record-type {{type}}`