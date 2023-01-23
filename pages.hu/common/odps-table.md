# odps table

> Táblák létrehozása és módosítása az ODPS-ben (Open Data Processing Service). Lásd még: `odps`. További információ: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Táblázat létrehozása partícióval és életciklussal:

`create table {{table_name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`

- Tábla létrehozása egy másik tábla definíciója alapján:

`create table {{table_name}} like {{another_table}};`

- Partíció hozzáadása egy táblához:

`alter table {{table_name}} add partition ({{partition_spec}});`

- Partíció törlése egy táblából:

`alter table {{table_name}} drop partition ({{partition_spec}});`

- Tábla törlése:

`drop table {{table_name}};`
