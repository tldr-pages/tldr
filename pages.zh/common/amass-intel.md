# amass intel

> 收集有关组织的开源情报，例如根域名和 ASN。
> 更多信息：<https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- 在一个 IP [addr] 地址范围内查找根域名：

`amass intel -addr {{192.168.0.1-254}}`

- 使用主动侦察方法：

`amass intel -active -addr {{192.168.0.1-254}}`

- 查找与某个 [d]omain 域名相关的根域名：

`amass intel -whois -d {{域名}}`

- 查找属于某个 [org]anisation 组织的 ASN：

`amass intel -org {{组织名称}}`

- 查找属于给定自治系统号的根域名：

`amass intel -asn {{自治系统号}}`

- 将结果保存到一个文本文件：

`amass intel -o {{输出文件}} -whois -d {{域名}}`

- 列出所有可用的数据源：

`amass intel -list`
