# hive

> CLI eszköz az Apache Hive-hoz. További információ: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>.

- Hive interaktív shell indítása:

`hive`

- A HiveQL futtatása:

`hive -e "{{hiveql_query}}"`

- HiveQL fájl futtatása változóhelyettesítéssel:

`hive --define {{key}}={{value}} -f {{path/to/file.sql}}`

- HiveQL futtatása HiveConfiggal (pl. `mapred.reduce.tasks=32`):

`hive --hiveconf {{conf_name}}={{conf_value}}`
