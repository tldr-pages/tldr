# sublist3r

> 快速子域名枚举工具，适用于渗透测试者。
> 更多信息请访问：<https://github.com/aboul3la/Sublist3r>。

- 查找某个域名的子域名：

`sublist3r --domain {{domain_name}}`

- 查找某个域名的子域名，并启用暴力搜索：

`sublist3r --domain {{domain_name}} --bruteforce`

- 将找到的子域名保存到文本文件中：

`sublist3r --domain {{domain_name}} --output {{path/to/output_file}}`

- 显示帮助信息：

`sublist3r --help`