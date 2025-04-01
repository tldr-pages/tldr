# mssqlclient.py

> 连接到 Microsoft SQL Server 实例并执行查询。
> 是 Impacket 套件的一部分。
> 更多信息：<https://github.com/fortra/impacket>.

- 使用 Windows 身份验证连接到 MSSQL 服务器：

`mssqlclient.py -windows-auth {{domain}}/{{username}}:{{password}}@{{target}}`

- 使用 SQL 服务器身份验证连接：

`mssqlclient.py {{username}}:{{password}}@{{target}}`

- 使用传递哈希身份验证连接：

`mssqlclient.py {{domain}}/{{username}}@{{target}} -hashes {{LM_Hash}}:{{NT_Hash}}`

- 使用 Kerberos 身份验证连接（需要有效的票据）：

`mssqlclient.py -k {{domain}}/{{username}}@{{target}}`

- 连接后执行特定的 SQL 命令：

`mssqlclient.py {{username}}:{{password}}@{{target}} -query "{{SELECT user_name();}}"`

- 从文件中执行多个 SQL 命令：

`mssqlclient.py {{username}}:{{password}}@{{target}} -file {{path/to/sql_file.sql}}`

- 连接到特定的数据库实例（默认为 `None`）：

`mssqlclient.py {{username}}:{{password}}@{{target}} -db {{database_name}}`

- 在执行前显示 SQL 查询：

`mssqlclient.py {{username}}:{{password}}@{{target}} -show`
