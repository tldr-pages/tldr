# odps table

> Crearea și modificarea tabelelor în ODPS (Open Data Processing Service).
> A se vedea, de asemenea, `odps`.
> Mai multe informaţii: <https://www.alibabacloud.com/help/doc-detail/27971.htm>

- Creați un tabel cu partiție și ciclu de viață:

`create table {{table_name}} ({{col}} {{type}}) partitioned by ({{col}} {{type}}) lifecycle {{days}};`

- Creați un tabel bazat pe definiția unui alt tabel:

`create table {{table_name}} like {{another_table}};`

- Adăugați partiție la un tabel:

`alter table {{table_name}} add partition ({{partition_spec}});`

- Ștergeți partiția dintr-un tabel:

`alter table {{table_name}} drop partition ({{partition_spec}});`

- Șterge tabelul:

`drop table {{table_name}};`
