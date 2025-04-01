# snowsql

> Snowflake 数据云的 SnowSQL 命令行客户端。
> 更多信息：<https://docs.snowflake.com/en/user-guide/snowsql.html>.

- 连接到 <https://account.snowflakecomputing.com> 上的特定实例（密码可以在提示中或配置文件中提供）：

`snowsql --accountname {{account}} --username {{username}} --dbname {{database}} --schemaname {{schema}}`

- 使用特定的配置文件连接到实例（默认为 `~/.snowsql/config`）：

`snowsql --config {{path/to/configuration_file}}`

- 使用多因素认证的令牌连接到默认实例：

`snowsql --mfa-passcode {{token}}`

- 在默认连接上执行单个 SQL 查询或 SnowSQL 命令（在 shell 脚本中有用）：

`snowsql --query '{{query}}'`

- 从特定文件中执行命令到默认连接：

`snowsql --filename {{path/to/file.sql}}`