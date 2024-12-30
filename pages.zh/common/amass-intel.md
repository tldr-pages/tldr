# 收集情报

> 收集关于一个组织的开放源代码情报，例如根域名和自治系统号（ASN）。
> 更多信息：<https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>。

- 在一个IP地址范围内查找根域名：

`amass intel -addr {{192.168.0.1-254}}`

- 使用主动侦查方法：

`amass intel -active -addr {{192.168.0.1-254}}`

- 查找与某个域名相关的根域名：

`amass intel -whois -d {{domain_name}}`

- 查找属于某个组织的ASN：

`amass intel -org {{organisation_name}}`

- 查找属于给定自治系统编号的根域名：

`amass intel -asn {{asn}}`

- 将结果保存到文本文件：

`amass intel -o {{output_file}} -whois -d {{domain_name}}`

- 列出所有可用的数据源：

`amass intel -list`