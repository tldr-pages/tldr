# hive

> Apache Hive 的命令行工具。
> 更多信息：<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>.

- 启动 Hive 交互式 shell:

`hive`

- 运行 HiveQL:

`hive -e "{{hiveql_query}}"`

- 使用变量替换运行 HiveQL 文件:

`hive --define {{key}}={{value}} -f {{path/to/file.sql}}`

- 使用 HiveConfig 运行 HiveQL（例如 `mapred.reduce.tasks=32`）:

`hive --hiveconf {{conf_name}}={{conf_value}}`
