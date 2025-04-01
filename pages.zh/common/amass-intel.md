# amass intel

> 收集有关组织的开源情报，如根域名和自治系统编号（ASNs）。
> 更多信息：<https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- 在 IP 地址范围内查找根域名：

`amass intel -addr {{192.168.0.1-254}}`

- 使用主动侦察方法：

`amass intel -active -addr {{192.168.0.1-254}}`

- 查找与域名相关联的根域名：

`amass intel -whois -d {{domain_name}}`

- 查找属于组织的自治系统编号（ASNs）：

`amass intel -org {{organisation_name}}`

- 查找属于指定自治系统编号的根域名：

`amass intel -asn {{asn}}`

- 将结果保存到文本文件：

`amass intel -o {{output_file}} -whois -d {{domain_name}}`

- 列出所有可用的数据源：

`amass intel -list`
