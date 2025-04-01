# httprobe

> 接受一个域名列表并探测可用的 HTTP 和 HTTPS 服务器。
> 更多信息：<https://github.com/tomnomnom/httprobe>.

- 从文本文件中读取域名列表并进行探测：

`cat {{input_file}} | httprobe`

- 如果 HTTPS 不可用时仅检查 HTTP：

`cat {{input_file}} | httprobe --prefer-https`

- 使用指定协议探测额外的端口：

`cat {{input_file}} | httprobe -p {{https:2222}}`

- 显示帮助信息：

`httprobe --help`