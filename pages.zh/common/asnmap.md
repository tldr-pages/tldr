# asnmap

> 一个使用 ASN 信息来映射组织网络范围的 Go CLI 工具。
> 注意：该工具需要来自 ProjectDiscovery Cloud Platform 的 API 密钥才能工作。
> 更多信息：<https://github.com/projectdiscovery/asnmap#usage>.

- 查询某个 ASN 的 CIDR 范围：

`asnmap {{[-a|-asn]}} {{AS5650}} -silent`

- 查询某个 IP 地址的 CIDR 范围：

`asnmap {{[-i|-ip]}} {{100.19.12.21}} -silent`

- 查询某个域名的 CIDR 范围：

`asnmap {{[-d|-domain]}} {{example.com}} -silent`

- 查询某个组织的 CIDR 范围：

`asnmap -org {{GOOGLE}} -silent`

- 从包含目标的文件中查询 CIDR 范围：

`asnmap {{[-f|-file]}} {{targets.txt}} -silent`

- 以 JSON 格式输出结果：

`asnmap {{[-d|-domain]}} {{facebook.com}} {{[-j|-json]}} -silent`

- 以 CSV 格式输出结果：

`asnmap {{[-a|-asn]}} {{AS394161}} {{[-c|-csv]}} -silent`

- 将 asnmap 更新到最新版本：

`asnmap {{[-up|-update]}}`
