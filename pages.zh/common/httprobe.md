# httprobe

> 从域名列表中探测有效的 HTTP 和 HTTPS 服务器。
> 更多信息：<https://github.com/tomnomnom/httprobe>。

- 从文本文件中探测域名列表：

`cat {{input_file}} | httprobe`

- 仅在 HTTPS 不工作时检查 HTTP：

`cat {{input_file}} | httprobe --prefer-https`

- 使用给定协议探测其他端口：

`cat {{input_file}} | httprobe -p {{https:2222}}`

- 显示帮助信息：

`httprobe --help`