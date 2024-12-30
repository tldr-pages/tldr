# hive

> Apache Hive 的 CLI 工具。
> 更多信息：<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>。

- 启动 Hive 交互式 shell：

`hive`

- 运行 HiveQL：

`hive -e "{{hiveql_query}}"`

- 运行带有变量替换的 HiveQL 文件：

`hive --define {{key}}={{value}} -f {{path/to/file.sql}}`

- 使用 HiveConfig 运行 HiveQL（例如 `mapred.reduce.tasks=32`）：

`hive --hiveconf {{conf_name}}={{conf_value}}`