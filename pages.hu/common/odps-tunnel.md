# odps tunnel

> Adatalagút az ODPS-ben (Open Data Processing Service). Lásd még: `odps`. További információ: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- Táblázat letöltése helyi fájlba:

`tunnel download {{table_name}} {{path/to/file}};`

- Helyi fájl feltöltése egy táblapartícióba:

`tunnel upload {{path/to/file}} {{table_name}}/{{partition_spec}};`

- Táblázat feltöltése a mező- és rekordhatárolók megadásával:

`tunnel upload {{path/to/file}} {{table_name}} -fd {{field_delim}} -rd {{record_delim}};`

- Táblázat feltöltése több szál használatával:

`tunnel upload {{path/to/file}} {{table_name}} -threads {{num}};`
