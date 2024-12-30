# snowsql

> SnowSQL 是 Snowflake 数据云的命令行客户端。
> 更多信息：<https://docs.snowflake.com/en/user-guide/snowsql.html>。

- 连接到特定实例，地址为 <https://account.snowflakecomputing.com> （密码可以在提示中或配置文件中提供）：

`snowsql --accountname {{account}} --username {{username}} --dbname {{database}} --schemaname {{schema}}`

- 连接到由特定配置文件指定的实例（默认值为 `~/.snowsql/config`）：

`snowsql --config {{path/to/configuration_file}}`

- 使用多因素认证的令牌连接到默认实例：

`snowsql --mfa-passcode {{token}}`

- 在默认连接上执行单个 SQL 查询或 SnowSQL 命令（在 shell 脚本中非常有用）：

`snowsql --query '{{query}}'`

- 从特定文件在默认连接上执行命令：

`snowsql --filename {{path/to/file.sql}}`