# mssqlclient.py

> Connect to Microsoft SQL Server instances and execute queries.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Connect to an MSSQL server using Windows authentication:

`mssqlclient.py -windows-auth {{domain}}/{{username}}:{{password}}@{{target}}`

- Connect using SQL server authentication:

`mssqlclient.py {{username}}:{{password}}@{{target}}`

- Connect using pass-the-hash authentication:

`mssqlclient.py {{domain}}/{{username}}@{{target}} -hashes {{LM_Hash}}:{{NT_Hash}}`

- Connect using Kerberos authentication (requires valid tickets):

`mssqlclient.py -k {{domain}}/{{username}}@{{target}}`

- Execute a specific SQL command upon connection:

`mssqlclient.py {{username}}:{{password}}@{{target}} -query "{{SELECT user_name();}}"`

- Execute multiple SQL commands from a file:

`mssqlclient.py {{username}}:{{password}}@{{target}} -file {{path/to/sql_file.sql}}`

- Connect to a specific database instance (default is `None`):

`mssqlclient.py {{username}}:{{password}}@{{target}} -db {{database_name}}`

- Display SQL queries before execution:

`mssqlclient.py {{username}}:{{password}}@{{target}} -show`
