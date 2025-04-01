# bloodhound-python

> 一个用于 BloodHound 的 Python 数据收集器，用于枚举 Active Directory 关系。
> 更多信息：<https://github.com/dirkjanm/BloodHound.py>。

- 使用默认的数据收集方法（包括组、会话和信任关系）收集所有数据：

`bloodhound-python --username {{username}} --password {{password}} --domain {{domain}}`

- 使用 Kerberos 认证方式收集数据，无需提供明文密码：

`bloodhound-python --collectionmethod {{All}} --kerberos --domain {{domain}}`

- 使用 NTLM 哈希而不是密码进行认证：

`bloodhound-python --collectionmethod {{All}} --username {{username}} --hashes {{LM:NTLM}} --domain {{domain}}`

- 为 DNS 查询指定自定义名称服务器：

`bloodhound-python --collectionmethod {{All}} --username {{username}} --password {{password}} --domain {{domain}} --nameserver {{nameserver}}`

- 将输出文件保存为压缩的 ZIP 文件：

`bloodhound-python --collectionmethod {{All}} --username {{username}} --password {{password}} --domain {{domain}} --zip`