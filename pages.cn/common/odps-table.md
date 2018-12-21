# odps table

> Create and modify tables in ODPS (Open Data Processing Service).

- Create a table with partition and lifecycle:

`create table {{table_name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`

- Create a table based on the definition of another table:

`create table {{table_name}} like {{another_table}};`

- Add partition to a table:

`alter table {{table_name}} add partition ({{partition_spec}});`

- Delete partition from a table:

`alter table {{table_name}} drop partition ({{partition_spec}});`

- Delete table:

`drop table {{table_name}};`
