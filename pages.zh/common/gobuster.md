# gobuster

> 对网络服务器及更多内容进行隐藏路径的暴力破解。
> 更多信息：<https://github.com/OJ/gobuster>。

- 发现与字典匹配的目录和文件：

`gobuster dir --url {{https://example.com/}} --wordlist {{path/to/file}}`

- 发现子域名：

`gobuster dns --domain {{example.com}} --wordlist {{path/to/file}}`

- 发现 Amazon S3 桶：

`gobuster s3 --wordlist {{path/to/file}}`

- 发现服务器上的其他虚拟主机：

`gobuster vhost --url {{https://example.com/}} --wordlist {{path/to/file}}`

- 模糊测试参数的值：

`gobuster fuzz --url {{https://example.com/?parameter=FUZZ}} --wordlist {{path/to/file}}`

- 模糊测试参数的名称：

`gobuster fuzz --url {{https://example.com/?FUZZ=value}} --wordlist {{path/to/file}}`