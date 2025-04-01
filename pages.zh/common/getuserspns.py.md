# GetUserSPNs.py

> 检索与 Active Directory 用户账户关联的服务主体名称 (SPN)。
> 属于 Impacket 套件。
> 更多信息：<https://github.com/fortra/impacket>.

- 枚举带有 SPN 的用户账户并请求其 Kerberos TGS 票据：

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}}`

- 使用传递哈希认证：

`GetUserSPNs.py {{domain}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -dc-ip {{domain_controller_ip}}`

- 将输出保存到文件：

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}} -outputfile {{output_file}}`

- 仅请求 TGS 票据：

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}} -request`

- 使用传递哈希认证仅请求 TGS 票据：

`GetUserSPNs.py {{domain}}/{{username}} -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} -request`
