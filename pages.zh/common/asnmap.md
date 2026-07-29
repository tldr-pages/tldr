# asnmap

> 使用 ASN 信息映射组织网络范围的 Go CLI 工具。
> 注意：需要 ProjectDiscovery Cloud Platform 的 API 密钥才能使工具工作。
> 更多信息：<https://github.com/projectdiscovery/asnmap#usage>。

- 查找 ASN 的 CIDR 范围：

`asnmap {{[-a|-asn]}} {{AS5650}} -silent`

- 查找 IP 地址的 CIDR 范围：

`asnmap {{[-i|-ip]}} {{100.19.12.21}} -silent`

- 查找域名的 CIDR 范围：

`asnmap {{[-d|-domain]}} {{example.com}} -silent`

- 查找组织的 CIDR 范围：

`asnmap -org {{GOOGLE}} -silent`

- 从目标文件查找 CIDR 范围：

`asnmap {{[-f|-file]}} {{路径/到/targets.txt}} -silent`

- 以 JSON 格式输出结果：

`asnmap {{[-d|-domain]}} {{facebook.com}} {{[-j|-json]}} -silent`

- 以 CSV 格式输出结果：

`asnmap {{[-a|-asn]}} {{AS394161}} {{[-c|-csv]}} -silent`

- 将 asnmap 更新到最新版本：

`asnmap {{[-up|-update]}}`
