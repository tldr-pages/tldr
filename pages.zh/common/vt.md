# vt

> VirusTotal 的命令行接口。
> 该命令需要 VirusTotal 账户的 API 密钥。
> 更多信息：<https://github.com/VirusTotal/vt-cli>。

- 扫描特定文件以检测病毒：

`vt scan file {{path/to/file}}`

- 扫描 URL 以检测病毒：

`vt scan url {{url}}`

- 显示特定分析的信息：

`vt analysis {{file_id|analysis_id}}`

- 以加密 Zip 格式下载文件（需要高级账户）：

`vt download {{file_id}} --output {{path/to/directory}} --zip --zip-password {{password}}`

- 初始化或重新初始化 `vt` 以交互方式输入 API 密钥：

`vt init`

- 显示有关域名的信息：

`vt domain {{url}}`

- 显示特定 URL 的信息：

`vt url {{url}}`

- 显示特定 IP 地址的信息：

`vt domain {{ip_address}}`