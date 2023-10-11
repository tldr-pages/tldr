# snowsql

> SnowSQL command-line client for Snowflake's Data Cloud.
> More information: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- Connect to a specific instance at <https://account.snowflakecomputing.com> (password can be provided in prompt or configuration file):

`snowsql --accountname {{account}} --username {{username}} --dbname {{database}} --schemaname {{schema}}`

- Connect to an instance specified by a specific configuration file (defaults to `~/.snowsql/config`):

`snowsql --config {{path/to/configuration_file}}`

- Connect to the default instance using a token for multi-factor authentication:

`snowsql --mfa-passcode {{token}}`

- Execute a single SQL query or SnowSQL command on the default connection (useful in shell scripts):

`snowsql --query '{{query}}'`

- Execute commands from a specific file on the default connection:

`snowsql --filename {{path/to/file.sql}}`
