# amass enum

> 查找某个域名的子域名。
> 更多信息：<https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- （被动）查找某个 [d]omain 的子域名：

`amass enum -d {{域名}}`

- 查找某个 [d]omain 的子域名，并通过尝试解析已发现的子域名来主动验证它们：

`amass enum -active -d {{域名}} -p {{80,443,8080}}`

- 对子 [d]omain 执行暴力搜索：

`amass enum -brute -d {{域名}}`

- 将结果保存到一个文本文件中：

`amass enum -o {{输出文件}} -d {{域名}}`

- 将终端输出保存到文件中，并将其他更详细的输出保存到一个目录中：

`amass enum -o {{输出文件}} -dir {{路径/到/目录}} -d {{域名}}`

- 列出所有可用的数据源：

`amass enum -list`
