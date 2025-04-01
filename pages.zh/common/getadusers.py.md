# GetADUsers.py

> 从 Active Directory 中检索用户列表，包括最后登录时间戳和电子邮件等属性。
> 是 Impacket 套件的一部分。
> 更多信息：<https://github.com/fortra/impacket>。

- 枚举所有 Active Directory 用户及其属性：

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- 仅检索特定用户的详细信息：

`GetADUsers.py -user {{user}} -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- 使用 pass-the-hash 身份验证提取用户详细信息：

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}`

- 将输出保存到文件：

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}} > output.txt`