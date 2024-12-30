# vt

> VirusTotal的命令行界面。
> 执行此命令需要VirusTotal账户的API密钥。
> 更多信息：<https://github.com/VirusTotal/vt-cli>。

- 扫描特定文件是否存在病毒：

`vt scan file {{path/to/file}}`

- 扫描URL是否存在病毒：

`vt scan url {{url}}`

- 显示特定分析的信息：

`vt analysis {{file_id|analysis_id}}`

- 以加密的Zip格式下载文件（需要高级账户）：

`vt download {{file_id}} --output {{path/to/directory}} --zip --zip-password {{password}}`

- 初始化或重新初始化`vt`以交互方式输入API密钥：

`vt init`

- 显示域的信息：

`vt domain {{url}}`

- 显示特定URL的信息：

`vt url {{url}}`

- 显示特定IP地址的信息：

`vt domain {{ip_address}}`