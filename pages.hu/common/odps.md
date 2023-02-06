# odps

> Aliyun ODPS (Open Data Processing Service) parancssori eszköz. Néhány alparancsnak, mint például a `odps inst`, saját használati dokumentációja van. További információ: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Indítsa el a parancssort egy egyéni konfigurációs fájl segítségével:

`odpscmd --config={{odps_config.ini}}`

- Switch current project:

`use {{project_name}};`

- Az aktuális projektben lévő táblázatok megjelenítése:

`show tables;`

- Egy táblázat leírása:

`desc {{table_name}};`

- Tábla partíciók megjelenítése:

`show partitions {{table_name}};`

- Egy partíció leírása:

`desc {{table_name}} partition ({{partition_spec}});`
