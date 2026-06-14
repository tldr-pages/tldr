# snowsql

> SnowSQL հաճախորդ Snowflake's Data Cloud-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.snowflake.com/en/user-guide/snowsql>:.

- Միացեք որոշակի օրինակին <https://account.snowflakecomputing.com> հասցեով (գաղտնաբառը կարող է տրամադրվել հուշում կամ կազմաձևման ֆայլում).:

`snowsql --accountname {{account}} --username {{username}} --dbname {{database}} --schemaname {{schema}}`

- Միացեք որոշակի կոնֆիգուրացիայի ֆայլի կողմից նշված օրինակին (կանխադրված է `~/.snowsql/config`):

`snowsql --config {{path/to/configuration_file}}`

- Միացեք լռելյայն օրինակին, օգտագործելով նշան՝ բազմագործոն նույնականացման համար.:

`snowsql --mfa-passcode {{token}}`

- Կատարեք մեկ SQL հարցում կամ SnowSQL հրաման լռելյայն կապի վրա (օգտակար կեղևի սցենարներում).:

`snowsql --query '{{query}}'`

- Կատարեք հրամաններ որոշակի ֆայլից լռելյայն կապի վրա.:

`snowsql --filename {{path/to/file.sql}}`
