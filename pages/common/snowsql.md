# snowsql

> SnowSQL command-line client for Snowflake's Data Cloud.
> More information: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- Connect to an instance at {{account}}.snowflakecomputing.com (password can be provided in prompt or configuration file):

`snowsql --accountname {{account}} --username {{username}} --dbname {{database}} --schemaname {{schema}}`

- Connect to an instance specified by the configuration file (by default, `~/.snowsql/config`):

`snowsql --config {{.snowsql/config}}`

- Connect to the default instance, specifying a MFA token:

`snowsql --mfa-passcode {{token}}`

- Execute a single SQL query or SnowSQL command on the default connection (useful in shell scripts):

`snowsql --query '{{query}}'`

- Execute commands from a file on the default connection:

`snowsql --filename {{path/to/file.sql}}`
