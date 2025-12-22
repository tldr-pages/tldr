# aws route53

> AWS Route53 的 CLI —— Route 53 是一个高可用且可扩展的域名系统（DNS）Web 服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/route53/>.

- 列出所有托管区域，包括私有和公共区域：

`aws route53 list-hosted-zones`

- 显示某个区域中的所有记录：

`aws route53 list-resource-record-sets --hosted-zone-id {{区域_id}}`

- 使用请求标识符创建一个新的公共区域，以便安全地重试该操作：

`aws route53 create-hosted-zone --name {{名称}} --caller-reference {{请求_标识符}}`

- 删除一个区域（如果该区域包含非默认的 SOA 和 NS 记录，此命令将失败）：

`aws route53 delete-hosted-zone --id {{区域_id}}`

- 使用 Amazon 服务器测试给定区域的 DNS 解析：

`aws route53 test-dns-answer --hosted-zone-id {{区域_id}} --record-name {{名称}} --record-type {{类型}}`
