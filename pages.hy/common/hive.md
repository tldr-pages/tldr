#փեթակ

> Գործիք Apache Hive-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>:.

- Սկսեք Hive ինտերակտիվ կեղևը.:

`hive`

- Գործարկել HiveQL:

`hive -e "{{hiveql_query}}"`

- Գործարկեք HiveQL ֆայլը փոփոխական փոխարինմամբ.:

`hive {{[-d|--define]}} {{key}}={{value}} -f {{path/to/file.sql}}`

- Գործարկեք HiveQL HiveConfig-ով (օրինակ՝ `mapred.reduce.tasks=32`):

`hive --hiveconf {{conf_name}}={{conf_value}}`
