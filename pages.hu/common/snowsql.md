# snowsql

> SnowSQL parancssori kliens a Snowflake adatfelhőhöz. További információ: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- Csatlakozás egy adott példányhoz a <https://account.snowflakecomputing.com> címen (a jelszó megadható a promptban vagy a konfigurációs fájlban):

`snowsql --accountname {{account}} --username {{username}} --dbname {{database}} --schemaname {{schema}}`

- Csatlakozás egy adott konfigurációs fájlban megadott példányhoz (alapértelmezett a `~/.snowsql/config`):

`snowsql --config {{path/to/configuration_file}}`

- Csatlakozás az alapértelmezett példányhoz a többfaktoros hitelesítéshez használt token segítségével:

`snowsql --mfa-passcode {{token}}`

- Egyetlen SQL-lekérdezés vagy SnowSQL-parancs végrehajtása az alapértelmezett kapcsolaton (hasznos a héjszkriptekben):

`snowsql --query '{{query}}'`

- Parancsok végrehajtása egy adott fájlból az alapértelmezett kapcsolaton:

`snowsql --filename {{path/to/file.sql}}`
