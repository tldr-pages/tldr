# odps

> Aliyun ODPS (Open Data Processing Service) command line tool.

- Start the command line with a custom configuration file:

`odpscmd --config={{odps_config.ini}}`

- Switch current project:

`use {{project_name}};`

- Show tables in the current project:

`show tables;`

- Describe a table:

`desc {{table_name}};`

- Show table partitions:

`show partitions {{table_name}};`

- Describe a partition:

`desc {{table_name}} partition ({{partition_spec}});`
