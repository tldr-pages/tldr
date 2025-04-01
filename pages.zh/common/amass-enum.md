# amass enum

> 查找域名的子域。
> 更多信息：<https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- 查找（被动地）域名的子域：

`amass enum -d {{domain_name}}`

- 查找域名的子域，并主动验证这些子域，尝试解析已找到的子域：

`amass enum -active -d {{domain_name}} -p {{80,443,8080}}`

- 对子域进行暴力搜索：

`amass enum -brute -d {{domain_name}}`

- 将结果保存到文本文件：

`amass enum -o {{output_file}} -d {{domain_name}}`

- 将终端输出保存到文件，并将其他详细输出保存到目录：

`amass enum -o {{output_file}} -dir {{path/to/directory}} -d {{domain_name}}`

- 列出所有可用的数据源：

`amass enum -list`
