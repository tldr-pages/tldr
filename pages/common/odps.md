# odps

> Aliyun ODPS command line tool.

- Start the command line:

`odpscmd --config {{odps_config.ini}}`

- Switch current project:

`use {{project_name}};`

- Show tables in the current project:

`show tables;`

- Show table partitions:

`show partitions {{table_name}};`

- Describe table/partition:

`desc {{table_name}} partition ({{partition_spec}});`

- Create a partitiond table with lifecycle:

`create table {{name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`

- Read the content of table:

`read {{table_name}} partition ({{partition_spec}}) {{limit}};`

- Download the table:

`tunnel download {{table_name}}/{{partition_spec}} {{file}};`

- Upload the table:

`tunnel upload {{file}} {{table_name}}/{{partition_spec}};`
