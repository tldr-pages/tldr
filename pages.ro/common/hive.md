# hive

> instrument CLI pentru Apache Hive.
> Mai multe informaţii: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>

- Porniți un înveliș interactiv Stup:

`hive`

- Rulați HIVEQL:

`hive -e "{{hiveql_query}}"`

- Rulați un fișier HiveQL cu o substituție variabilă:

`hive --define {{key}}={{value}} -f {{path/to/file.sql}}`

- Rulați un HiveQL cu HiveConfig (de exemplu `mapred.reduce.tasks=32`):

`hive --hiveconf {{conf_name}}={{conf_value}}`
