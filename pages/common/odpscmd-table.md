# odpscmd table

> Create and modify tables in ODPS (Open Data Processing Service).
> See also: `odps`.
> More information: <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>.

- [Interactive] Create a table with partition and lifecycle:

`create table {{table_name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`

- [Interactive] Create a table based on the definition of another table:

`create table {{table_name}} like {{another_table}};`

- [Interactive] Add partition to a table:

`alter table {{table_name}} add partition ({{partition_spec}});`

- [Interactive] Delete partition from a table:

`alter table {{table_name}} drop partition ({{partition_spec}});`

- [Interactive] Delete table:

`drop table {{table_name}};`
