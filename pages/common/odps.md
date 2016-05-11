# odps

> Aliyun ODPS (Open Data Processing Service) command line tool.

- Start the command line with a custom configuration file:

`odpscmd --config {{odps_config.ini}}`

- Switch current project:

`use {{project_name}};`

- Show tables in the current project:

`show tables;`

- Show table partitions:

`show partitions {{table_name}};`

- Describe table partition:

`desc {{table_name}} partition ({{partition_spec}});`

- Create a partitiond table with lifecycle:

`create table {{name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`
